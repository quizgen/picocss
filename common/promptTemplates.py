from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from typing import List

class QuizMultipleChoice(BaseModel):
    questions: List[str] = Field(description="The quiz questions")
    alternatives: List[List[str]] = Field(description="The quiz alternatives")
    answers: List[str] = Field(description="The quiz answers")

class QuizTrueFalse(BaseModel):
    questions: List[str] = Field(description="The quiz questions")
    alternatives: List[List[str]] = Field(description="The quiz alternatives")
    answers: List[str] = Field(description="The quiz answers")

class QuizOpenEnded(BaseModel):
    questions: List[str] = Field(description="The quiz questions")
    answers: List[str] = Field(description="The quiz answers")

class QuizShortAnswer(BaseModel):
    questions: List[str] = Field(description="The quiz questions")
    answers: List[str] = Field(description="The quiz answers")

def create_quiz_chain(prompt_template, llm, pydantic_object_schema):
    return prompt_template | llm.with_structured_output(pydantic_object_schema)

# def create_multiple_choice_template(language):
#     template = """ 
#     You are an expert quiz maker for technical fields. Let's think step by step and
#     create a {difficulty} quiz with {num_questions} multiple-choice questions about the following concept/content: {quiz_context}.
#     {user_input}
#     The format of the quiz should be as follows:
#     - Multiple-choice: 
#     - Questions:
#         <Question1>: 
#             - Alternatives1: <option 1>, <option 2>, <option 3>, <option 4>
#         <Question2>: 
#             - Alternatives2: <option 1>, <option 2>, <option 3>, <option 4>
#         ....
#         <QuestionN>: 
#             - AlternativesN: <option 1>, <option 2>, <option 3>, <option 4>
#     - Answers:
#         <Answer1>: <option 1 | option 2 | option 3 | option 4>
#         <Answer2>: <option 1 | option 2 | option 3 | option 4>
#         ....
#         <AnswerN>: <option 1 | option 2 | option 3 | option 4>
#     """
#     if language != 'English':
#         template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
#     return ChatPromptTemplate.from_template(template)

# def create_true_false_template(language):
#     template = """
#     You are an expert quiz maker for technical fields. Let's think step by step and
#     create a {difficulty} quiz with {num_questions} true/false quiz about the following concept/content: {quiz_context}.
#     {user_input}
#     The format of the quiz should be as follows:
#     - Questions:
#         <Question1>: 
#             - Alternatives1: <True>, <False>
#         <Question2>: 
#             - Alternatives2: <True>, <False>
#         .....
#         <QuestionN>: 
#             - AlternativesN: <True>, <False>
#     - Answers:
#         <Answer1>: <True|False>
#         <Answer2>: <True|False>
#         .....
#         <AnswerN>: <True|False>
#     """
#     if language != 'English':
#         template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
#     return ChatPromptTemplate.from_template(template)

# def create_open_ended_template(language):
#     template = """
#     You are an expert quiz maker for technical fields. Let's think step by step and
#     create a {difficulty} quiz with {num_questions} open-ended quiz about the following concept/content: {quiz_context}.
#     {user_input}
#     The format of the quiz should be as follows:
#     - Questions:
#         <Question1>: 
#         <Question2>:
#         .....
#         <QuestionN>:
#     - Answers:    
#         <Answer1>:
#         <Answer2>:
#         .....
#         <AnswerN>:
#     """
#     if language != 'English':
#         template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
#     return ChatPromptTemplate.from_template(template)

# def create_short_answer_template(language):
#     template = """
#     You are an expert quiz maker for technical fields. Let's think step by step and
#     create a {difficulty} quiz with {num_questions} short-answer questions about the following concept/content: {quiz_context}.
#     {user_input}
#     The format of the quiz should be as follows:
#     - Questions:
#         <Question1>: 
#         <Question2>:
#         .....
#         <QuestionN>:
#     - Answers:
#         Provide a concise and specific answer in one or two words for each question. The answer should be brief and to the point.
#         <Answer1>:
#         <Answer2>:
#         .....
#         <AnswerN>:
#     """
#     if language != 'English':
#         template += f"Now, please translate the entire quiz into {language}, ensuring that the technical accuracy and clarity of the questions and answers are maintained."
#     return ChatPromptTemplate.from_template(template)



# promptTemplates.py에서의 프롬프트 부분 수정
def create_multiple_choice_template(language):
    template = """ 
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} multiple-choice questions about the following concept/content: {quiz_context}.
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "alternatives": [
            ["<option 1>", "<option 2>", "<option 3>", "<option 4>"],
            ...
        ],
        "answers": [
            "<Answer1>",
            ... 
        ]
    }}

    Ensure that the questions are relevant, the alternatives are challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
    return ChatPromptTemplate.from_template(template)

def create_true_false_template(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} true/false questions about the following concept/content: {quiz_context}.
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "alternatives": [
            ["True", "False"],
            ...
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Ensure that the questions are relevant, the alternatives are challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
    return ChatPromptTemplate.from_template(template)

def create_open_ended_template(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} open-ended questions about the following concept/content: {quiz_context}.
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Ensure that the questions are relevant and challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and answers."
    return ChatPromptTemplate.from_template(template)

def create_short_answer_template(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} short-answer questions about the following concept/content: {quiz_context}.
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Provide a concise and specific answer for each question in one or two words.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and answers."
    return ChatPromptTemplate.from_template(template)


def create_multiple_choice_template_keyword(language):
    template = """ 
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} multiple-choice questions about the following concept/content: {quiz_context}.
    The questions should focus specifically on the following keyword: "{keyword}". 
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "alternatives": [
            ["<option 1>", "<option 2>", "<option 3>", "<option 4>"],
            ...
        ],
        "answers": [
            "<Answer1>",
            ... 
        ]
    }}

    Ensure that the questions are relevant to the keyword, the alternatives are challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
    return ChatPromptTemplate.from_template(template)

def create_true_false_template_keyword(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} true/false questions about the following concept/content: {quiz_context}.
    The questions should focus specifically on the following keyword: "{keyword}". 
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "alternatives": [
            ["True", "False"],
            ...
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Ensure that the questions are relevant to the keyword, the alternatives are challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and options."
    return ChatPromptTemplate.from_template(template)


def create_open_ended_template_keyword(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} open-ended questions about the following concept/content: {quiz_context}.
    The questions should focus specifically on the following keyword: "{keyword}". 
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Ensure that the questions are relevant and challenging, and the answers are accurate.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and answers."
    return ChatPromptTemplate.from_template(template)

def create_short_answer_template_keyword(language):
    template = """
    You are an expert quiz maker for technical fields. Let's think step by step and
    create a {difficulty} quiz with {num_questions} short-answer questions about the following concept/content: {quiz_context}.
    The questions should focus specifically on the following keyword: "{keyword}". 
    {user_input}문제를 한국어로 생성해주세요.
    The format of the quiz should be a JSON object structured as follows:

    {{
        "questions": [
            "<Question1>",
            "<Question2>",
            ...
            "<QuestionN>"
        ],
        "answers": [
            "<Answer1>",
            ...
        ]
    }}

    Provide a concise and specific answer for each question in one or two words.
    """
    if language != 'English':
        template += f"\n\nPlease ensure that the quiz is accurately translated into {language}, maintaining the technical accuracy and clarity of the questions and answers."
    return ChatPromptTemplate.from_template(template)
