from fasthtml.common import *
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 환경 변수 로드
load_dotenv()

# 챗 모델 초기화
chat_model = ChatOpenAI()

# FastHTML 앱 생성
app = FastHTML(hdrs=("pico",))

# 공통 네비게이션 바 생성
def create_nav():
    return Nav(
        Div(
            # 로고 부분 추가
            Div(
                H1("QuizGen", cls="logo"),
                cls="brand"
            ),
            # 네비게이션 링크 및 검색 바 추가
            Ul(
                Li(A("강의계획서", href="/course-plan")),
                Li(A("강의계획서 목록", href="/course-plan/list")),
                Li(A("키워드 입력", href="/")),
                Li(A("텍스트 입력", href="/text")),
                Li(A("PDF 업로드", href="/pdf")),
                Li(A("URL 입력", href="/url")),
                Li(A("유튜브 링크", href="/youtube")),
                Li(A("비디오 업로드", href="/video")),
                cls="navigation-links"
            ),
            # 검색 바 추가
            Form(
                Input(type="search", placeholder="Search...", name="search"),
                Button("검색", type="submit"),
                cls="search-bar"
            ),
            cls="container-fluid"  # 네비게이션 바를 전체 너비로 확장
        )
    )


# 공통 헤더 생성
def create_header(description):
    return Header(
        create_nav(),  # 네비게이션 바를 가장 위로 배치
        Div(
            P(description),  # 동적으로 변경 가능한 설명 문구
            cls="container"
        ),
        cls="container"
    )


# 공통 푸터 생성
def create_footer():
    return Footer(
        P(Small("© 2024. QuizGen. All rights reserved.")),
        cls="container"
    )

# 메인 페이지 (키워드 입력)
@app.get("/")
def home():
    return Html(
        Head(
            Title("QuizGen • 키워드 입력"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("키워드를 입력 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("키워드를 입력해 주세요"),
                    Form(
                        Label("키워드를 입력해 주십시오. 예) 인공지능", Textarea(placeholder="예) 인공지능", rows="2")),
                        Label("서브 키워드를 선택하세요:", Select(
                            Option("Choose an option", value="", selected=True),
                            Option("인공지능"),
                            Option("컴퓨터 비전"),
                            Option("자연어 처리")
                        )),
                        Div(  # 언어, 종류 선택, 난이도, LLM을 가로로 정렬
                            Fieldset(
                                Legend("언어 선택"),
                                Label("한국어", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid"  # 가로로 배치
                        ),
                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="요구사항을 입력하세요...")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# 강의계획서 목록 페이지
@app.get("/course-plan/list")
def course_plan_list():
    return Html(
        Head(
            Title("강의계획서 목록 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("강의계획서."),  # 설명 문구 전달
            Main(
                Section(
                    H2("강의계획서 목록"),
                    P("강의계획서를 선택하세요."),
                    Ul(
                        Li(A("강의계획서 1", href="/course-plan/1")),
                        Li(A("강의계획서 2", href="/course-plan/2")),
                        Li(A("강의계획서 3", href="/course-plan/3")),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )

# 개별 강의계획서 페이지
@app.get("/course-plan/{id}")
def course_plan(id: str):
    return Html(
        Head(
            Title(f"강의계획서 {id} • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("강의계획서"),  # 설명 문구 전달
            Main(
                Section(
                    H2(f"강의계획서 {id}"),
                    Textarea(placeholder=f"강의계획서 {id} 내용을 입력하세요.", rows="10"),
                    Button("수정", type="submit", cls="primary"),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )

# 텍스트 입력 페이지
@app.get("/text")
def text_input():
    return Html(
        Head(
            Title("텍스트 입력 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("text를 입력 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("텍스트를 입력해 주세요"),
                    Form(
                        Label("텍스트(긴 글) 입력란", Textarea(placeholder="예) 인공지능이란....", rows="5")),
                        Div(
                            Div(
                                H3("기본 입력"),
                                Button("기본 입력"),
                                Button("내용 확인"),
                                cls="container"
                            ),
                            Div(
                                H3("키워드 추출"),
                                Button("키워드 추출"),
                                cls="container"
                            ),
                            cls="grid"
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("Korean", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid",
                            style="margin-top: 30px;"  # 여백 추가

    
                        ),
                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="문제를 한국어로 생성해 주세요.")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# PDF 업로드 페이지
@app.get("/pdf")
def pdf_upload():
    return Html(
        Head(
            Title("PDF 업로드 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("pdf를 업로드 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("PDF 파일 업로드"),
                    Form(
                        Label("Drag and drop file here", Input(type="file", accept=".pdf")),
                        Div(
                            Div(
                                H3("기본 입력"),
                                Button("기본 입력"),
                                Button("내용 확인"),
                                cls="container"
                            ),
                            cls="grid"
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("Korean", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid",
                            style="margin-top: 30px;"  # 여백 추가
                        ),


                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="문제를 한국어로 생성해 주세요.")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# URL 입력 페이지
@app.get("/url")
def url_input():
    return Html(
        Head(
            Title("URL 입력 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("url 를 입력 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("URL 입력"),
                    Form(
                        Label("URL 입력란 (예: https://ko.wikipedia.org/wiki/)", Input(type="url", placeholder="https://")),
                        Div(
                            Div(
                                H3("기본 입력"),
                                Button("기본 입력"),
                                Button("내용 확인"),
                                cls="container"
                            ),
                            cls="grid"
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("Korean", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid",
                            style="margin-top: 30px;"  # 여백 추가
                        ),

                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="문제를 한국어로 생성해 주세요.")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# 유튜브 링크 입력 페이지
@app.get("/youtube")
def youtube_input():
    return Html(
        Head(
            Title("유튜브 링크 입력 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("youtube 링크를 입력 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("유튜브 주소 입력 후 원하는 문제를 선택하여 주십시오."),
                    Form(
                        Label("유튜브 URL 입력란 (예: https://youtu.be/)", Input(type="url", placeholder="https://youtu.be/")),
                        Div(
                            Div(
                                H3("기본 입력"),
                                Button("기본 입력"),
                                Button("내용 확인"),
                                cls="container"
                            ),
                            cls="grid"
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("Korean", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid",
                            style="margin-top: 30px;"  # 여백 추가
                        ),

                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="문제를 한국어로 생성해 주세요.")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# 비디오 업로드 페이지
@app.get("/video")
def video_upload():
    return Html(
        Head(
            Title("비디오 업로드 • QuizGen"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
        ),
        Body(
            create_header("video를 업로드 후 원하는 문제 유형을 선택하여 주십시오."),  # 설명 문구 전달
            Main(
                Section(
                    H2("비디오 파일을 업로드해 주세요."),
                    Form(
                        Label("Drag and drop file here", Input(type="file", accept="video/*")),      
                        Div(
                            Div(
                                H3("기본 입력"),
                                Button("기본 입력"),
                                Button("내용 확인"),
                                cls="container"
                            ),
                            cls="grid"
                        ),
                        Div(
                            Fieldset(
                                Legend("언어 선택"),
                                Label("Korean", Input(type="radio", name="language", value="korean", checked=True)),
                                Label("English", Input(type="radio", name="language", value="english"))
                            ),
                            Fieldset(
                                Legend("종류 선택"),
                                Label("객관식", Input(type="radio", name="type", value="multiple-choice", checked=True)),
                                Label("참/거짓", Input(type="radio", name="type", value="true-false")),
                                Label("주관식", Input(type="radio", name="type", value="short-answer")),
                                Label("단답형", Input(type="radio", name="type", value="open-ended"))
                            ),
                            Fieldset(
                                Legend("난이도"),
                                Label("easy", Input(type="radio", name="difficulty", value="easy")),
                                Label("normal", Input(type="radio", name="difficulty", value="normal", checked=True)),
                                Label("hard", Input(type="radio", name="difficulty", value="hard"))
                            ),
                            Fieldset(
                                Legend("LLM"),
                                Label("gpt-4-turbo", Input(type="radio", name="llm", value="gpt-4-turbo")),
                                Label("gpt-4o-mini", Input(type="radio", name="llm", value="gpt-4o-mini", checked=True)),
                                Label("gpt-4o", Input(type="radio", name="llm", value="gpt-4o")),
                                Label("Llama3.1-70b", Input(type="radio", name="llm", value="llama3-70b"))
                            ),
                            cls="grid",
                            style="margin-top: 30px;"  # 여백 추가
                        ),
                        Label("갯수 선택", Input(type="number", value="3", min="1", max="10")),
                        Label("기타 요구 사항을 입력해 주세요", Textarea(placeholder="문제를 한국어로 생성해 주세요.")),
                        Button("퀴즈 생성", type="submit"),
                        cls="container"
                    ),
                    cls="container"
                ),
                cls="container"
            ),
            create_footer()
        )
    )


# 서버 실행
serve()
