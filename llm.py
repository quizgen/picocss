from fastcore.parallel import threaded
from fasthtml.common import *
import os, uvicorn
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from threading import Lock

# 환경 변수 로드
load_dotenv()

# FastHTML 앱 설정
app = FastHTML(live=True, hdrs=("pico",))

# LangChain ChatOpenAI 설정
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 생성된 문제 저장
quizzes = []
quiz_lock = Lock()

# 단순 프롬프트를 사용하여 문제 생성
def generate_quiz_simple(quiz_type, language, num_questions, context, difficulty, user_input):
    try:
        print(f"Generating quiz with parameters: quiz_type={quiz_type}, language={language}, "
              f"num_questions={num_questions}, context={context}, difficulty={difficulty}, user_input={user_input}")

        # 프롬프트 생성
        prompt = f"""
        You are an expert quiz maker. Create a {difficulty} level quiz in {language}.
        Quiz Type: {quiz_type}
        Number of Questions: {num_questions}
        Topic: {context}
        Additional Instructions: {user_input}
        
        Please provide the quiz as a JSON object with the following format:
        {{
            "questions": ["Question 1", "Question 2", ...],
            "options": [["Option 1.1", "Option 1.2", ...], ...],  # Only for multiple-choice
            "answers": ["Answer 1", "Answer 2", ...]
        }}
        """
        print(f"Generated Prompt:\n{prompt}")

        # LLM 호출
        response = llm.predict(prompt)
        print(f"Generated Quiz:\n{response}")
        return response
    except Exception as e:
        error_message = f"Error in generate_quiz_simple: {str(e)}"
        print(error_message)
        return error_message

# 상태 업데이트 함수
def quiz_preview(id):
    if id < len(quizzes):
        return Div(f"<p>Generated Quiz: {quizzes[id]}</p>", id='quiz-list')
    else:
        return Div("<p>Generating quiz...</p>", id='quiz-list', 
                   hx_post=f"/quizzes/{id}",
                   hx_trigger="every 1s", hx_swap="outerHTML")

# 상태 확인 라우트
@app.post("/quizzes/{id}")
def get_quiz(id: int): 
    return quiz_preview(id)

# 문제 생성 요청 처리
@app.post("/")
def post(quiz_type: str, language: str, num_questions: int, context: str, difficulty: str, user_input: str):
    print(f"POST Request Parameters -> quiz_type: {quiz_type}, language: {language}, "
          f"num_questions: {num_questions}, context: {context}, difficulty: {difficulty}, user_input: {user_input}")
    id = len(quizzes)
    generate_quiz_thread_simple(quiz_type, language, num_questions, context, difficulty, user_input, id)
    return Div(id='quiz-list', children=[quiz_preview(id)])

@threaded
def generate_quiz_thread_simple(quiz_type, language, num_questions, context, difficulty, user_input, id):
    try:
        print(f"Generating quiz for ID: {id}")
        quiz_data = generate_quiz_simple(quiz_type, language, num_questions, context, difficulty, user_input)
        
        # 스레드 안전성 보장
        with quiz_lock:
            quizzes.append(quiz_data)
    except Exception as e:
        error_message = f"Error generating quiz for ID {id}: {str(e)}"
        print(error_message)  # 상세 오류 로그 출력
        with quiz_lock:
            quizzes.append(error_message)

# 공통 네비게이션 바 생성
def create_nav():
    return Nav(
        Div(
            Div(H1("QuizGen", cls="logo"), cls="brand"),
            Ul(
                Li(A("강의계획서", href="/course-plan")),
                Li(A("강의계획서 목록", href="/course-plan/list")),
                Li(A("키워드 입력", href="/")),
                cls="navigation-links"
            ),
            Form(
                Input(type="search", placeholder="Search...", name="search"),
                Button("검색", type="submit"),
                cls="search-bar"
            ),
            cls="container-fluid"
        )
    )

# 공통 헤더 생성
def create_header(description):
    return Header(
        create_nav(),
        Div(P(description), cls="container"),
        cls="container"
    )

# 공통 푸터 생성
def create_footer():
    return Footer(P(Small("© 2024. QuizGen. All rights reserved.")), cls="container")

@app.get("/")
def home():
    return Html(
        Head(
            Title("QuizGen • 키워드 입력"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("키워드를 입력 후 원하는 문제 유형을 선택하여 주십시오."),
            Main(
                Section(
                    H2("키워드를 입력해 주세요"),
                    Form(
                        Group(
                            Label("키워드를 입력해 주십시오:", 
                                Textarea(name="context", placeholder="예) 인공지능", rows="2")
                            )
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("한국어", Input(type="radio", name="language", value="한국어", checked=True)),
                                Label("English", Input(type="radio", name="language", value="English"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="quiz_type", value="객관식", checked=True)),
                                Label("참/거짓", Input(type="radio", name="quiz_type", value="참/거짓")),
                                Label("주관식", Input(type="radio", name="quiz_type", value="주관식")),
                                Label("단답형", Input(type="radio", name="quiz_type", value="단답형"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            cls="grid"
                        ),
                        Label("갯수 선택", 
                            Input(type="number", name="num_questions", value="3", min="1", max="10")
                        ),
                        Label("기타 요구 사항을 입력해 주세요", 
                            Textarea(name="user_input", placeholder="요구사항을 입력하세요...")
                        ),
                        Button("퀴즈 생성", method="post", hx_post="/", target_id='quiz-list', hx_swap="innerHTML"),
                        cls="container"
                    ),
                    Div(id='quiz-list')
                ),
                cls="container"
            ),
            create_footer()
        )
    )

# 서버 실행
if __name__ == '__main__':
    uvicorn.run("llm:app", host='0.0.0.0', port=int(os.getenv("PORT", default=5000)))
