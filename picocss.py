# from fasthtml.common import *
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# # Load environment variables
# load_dotenv()

# # Initialize the chat model
# chat_model = ChatOpenAI()

# # # Create the FastHTML app
# app = FastHTML(hdrs=(picolink))


# # 공통 네비게이션 바 생성
# def create_nav():
#     return Nav(
#         Ul(
#             Li(A(Button("Home", cls="primary"), href="/")),
#             Li(A(Button("Preview", cls="secondary"), href="/preview")),
#             Li(A(Button("Typography", cls="contrast"), href="/typography")),
#             Li(A(Button("Buttons", cls="outline"), href="/buttons")),
#             Li(A(Button("Form Elements", cls="outline secondary"), href="/form")),
#             Li(A(Button("Tables", cls="outline contrast"), href="/tables")),
#             Li(A(Button("Modal", cls="primary"), href="/modal")),
#             Li(A(Button("Accordions", cls="secondary"), href="/accordions")),
#             Li(A(Button("Article", cls="contrast"), href="/article")),
#             Li(A(Button("Group", cls="outline"), href="/group")),
#             Li(A(Button("Progress", cls="outline secondary"), href="/progress")),
#             Li(A(Button("Loading", cls="outline contrast"), href="/loading")),
#             cls="menu"
#         ),
#         cls="container"
#     )




# # 공통 헤더 생성
# def create_header():
#     return Header(
#         Div(
#             H1("Pico"),
#             P("A pure HTML example, without dependencies."),
#             cls="container"
#         ),
#         create_nav(),
#         cls="container"
#     )

# # 공통 푸터 생성
# def create_footer():
#     return Footer(
#         P(Small(
#             "Built with ", A("Pico", href="https://picocss.com"), " • ",
#             A("Source code", href="https://github.com/picocss/examples/blob/master/v2-html/index.html")
#         )),
#         cls="container"
#     )

# # 메인 페이지
# @app.get("/")
# def home():
#     return Html(
#         Head(
#             Title("Home • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Welcome to the PicoCSS Example"),
#                     P("Use the navigation bar to explore different components."),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Preview 페이지
# @app.get("/preview")
# def preview():
#     return Html(
#         Head(
#             Title("Preview • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Preview"),
#                     P("Sed ultricies dolor non ante vulputate hendrerit. Vivamus sit amet suscipit sapien."),
#                     Form(
#                         Div(
#                             Input(type="text", name="firstname", placeholder="First name", required=True),
#                             Input(type="email", name="email", placeholder="Email address", required=True),
#                             Button("Subscribe", type="submit"),
#                             cls="grid"
#                         ),
#                         Fieldset(
#                             Label(
#                                 Input(type="checkbox", role="switch", id="terms", name="terms"),
#                                 "I agree to the ",
#                                 A("Privacy Policy", href="#", onclick="event.preventDefault()")
#                             )
#                         )
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Typography 페이지
# @app.get("/typography")
# def typography():
#     return Html(
#         Head(
#             Title("Typography • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Typography"),
#                     P("Aliquam lobortis vitae nibh nec rhoncus. Morbi mattis neque eget efficitur feugiat."),
#                     Blockquote(
#                         "Maecenas vehicula metus tellus, vitae congue turpis hendrerit non. Nam at dui sit amet ipsum cursus ornare.",
#                         Footer(Cite("- Phasellus eget lacinia"))
#                     ),
#                     H3("Lists"),
#                     Ul(
#                         Li("Aliquam lobortis lacus eu libero ornare facilisis."),
#                         Li("Nam et magna at libero scelerisque egestas."),
#                         Li("Suspendisse id nisl ut leo finibus vehicula quis eu ex."),
#                         Li("Proin ultricies turpis et volutpat vehicula.")
#                     ),
#                     H3("Inline text elements"),
#                     Div(
#                         P(A("Primary link", href="#", onclick="event.preventDefault()")),
#                         P(A("Secondary link", href="#", onclick="event.preventDefault()", cls="secondary")),
#                         P(A("Contrast link", href="#", onclick="event.preventDefault()", cls="contrast")),
#                         cls="grid"
#                     ),
#                     Div(
#                         P(Strong("Bold")),
#                         P(Em("Italic")),
#                         P(U("Underline")),
#                         cls="grid"
#                     ),
#                     Div(
#                         P(Del("Deleted")),
#                         P(Ins("Inserted")),
#                         P(S("Strikethrough")),
#                         cls="grid"
#                     ),
#                     Div(
#                         P(Small("Small")),
#                         P("Text ", Sub("Sub")),
#                         P("Text ", Sup("Sup")),
#                         cls="grid"
#                     ),
#                     Div(
#                         P(Abbr("Abbr.", title="Abbreviation", data_tooltip="Abbreviation")),
#                         P(Kbd("Kbd")),
#                         P(Mark("Highlighted")),
#                         cls="grid"
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Buttons 페이지
# @app.get("/buttons")
# def buttons():
#     return Html(
#         Head(
#             Title("Buttons • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Buttons"),
#                     P(
#                         Button("Primary"),
#                         Button("Secondary", cls="secondary"),
#                         Button("Contrast", cls="contrast"),
#                         cls="grid"
#                     ),
#                     P(
#                         Button("Primary outline", cls="outline"),
#                         Button("Secondary outline", cls="outline secondary"),
#                         Button("Contrast outline", cls="outline contrast"),
#                         cls="grid"
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Form Elements 페이지
# @app.get("/form")
# def form_elements():
#     return Html(
#         Head(
#             Title("Form Elements • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Form elements"),
#                     Form(
#                         Label("Search", Input(type="search", id="search", name="search", placeholder="Search")),
#                         Label("Text", Input(type="text", id="text", name="text", placeholder="Text")),
#                         Small("Curabitur consequat lacus at lacus porta finibus."),
#                         Label("Select", Select(
#                             Option("Select…", value="", selected=True),
#                             Option("…")
#                         )),
#                         Label("File browser", Input(type="file", id="file", name="file")),
#                         Label("Range slider", Input(type="range", min="0", max="100", value="50", id="range", name="range")),
#                         Div(
#                             Label("Valid", Input(type="text", id="valid", name="valid", placeholder="Valid", aria_invalid="false")),
#                             Label("Invalid", Input(type="text", id="invalid", name="invalid", placeholder="Invalid", aria_invalid="true")),
#                             Label("Disabled", Input(type="text", id="disabled", name="disabled", placeholder="Disabled", disabled=True)),
#                             cls="grid"
#                         ),
#                         Div(
#                             Label("Date", Input(type="date", id="date", name="date")),
#                             Label("Time", Input(type="time", id="time", name="time")),
#                             Label("Color", Input(type="color", id="color", name="color", value="#0eaaaa")),
#                             cls="grid"
#                         ),
#                         Div(
#                             Fieldset(
#                                 Legend(Strong("Checkboxes")),
#                                 Label("Checkbox", Input(type="checkbox", id="checkbox-1", name="checkbox-1", checked=True)),
#                                 Label("Checkbox", Input(type="checkbox", id="checkbox-2", name="checkbox-2"))
#                             ),
#                             Fieldset(
#                                 Legend(Strong("Radio buttons")),
#                                 Label("Radio button", Input(type="radio", id="radio-1", name="radio", value="radio-1", checked=True)),
#                                 Label("Radio button", Input(type="radio", id="radio-2", name="radio", value="radio-2"))
#                             ),
#                             Fieldset(
#                                 Legend(Strong("Switches")),
#                                 Label("Switch", Input(type="checkbox", id="switch-1", name="switch-1", role="switch", checked=True)),
#                                 Label("Switch", Input(type="checkbox", id="switch-2", name="switch-2", role="switch"))
#                             ),
#                             cls="grid"
#                         ),
#                         Div(
#                             Input(type="reset", value="Reset", onclick="event.preventDefault()"),
#                             Input(type="submit", value="Submit", onclick="event.preventDefault()"),
#                             cls="grid"
#                         )
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Tables 페이지
# @app.get("/tables")
# def tables():
#     return Html(
#         Head(
#             Title("Tables • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Tables"),
#                     Div(
#                         Table(
#                             Thead(
#                                 Tr(
#                                     Th("#", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col"),
#                                     Th("Heading", scope="col")
#                                 )
#                             ),
#                             Tbody(
#                                 Tr(
#                                     Th("1", scope="row"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell")
#                                 ),
#                                 Tr(
#                                     Th("2", scope="row"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell")
#                                 ),
#                                 Tr(
#                                     Th("3", scope="row"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell"),
#                                     Td("Cell")
#                                 )
#                             ),
#                             cls="striped"
#                         ),
#                         cls="overflow-auto"
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Modal 페이지
# @app.get("/modal")
# def modal():
#     return Html(
#         Head(
#             Title("Modal • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Modal"),
#                     Button(
#                         "Launch demo modal", 
#                         cls="contrast", 
#                         data_target="modal-example", 
#                         onclick="toggleModal(event)"
#                     ),
#                     Dialog(
#                         Article(
#                             Header(
#                                 Button(
#                                     aria_label="Close", 
#                                     rel="prev", 
#                                     data_target="modal-example", 
#                                     onclick="toggleModal(event)"
#                                 ),
#                                 H3("Confirm your action!")
#                             ),
#                             P("Cras sit amet maximus risus. Pellentesque sodales odio sit amet augue finibus pellentesque."),
#                             Footer(
#                                 Button("Cancel", role="button", cls="secondary", data_target="modal-example", onclick="toggleModal(event)"),
#                                 Button("Confirm", autofocus=True, data_target="modal-example", onclick="toggleModal(event)")
#                             )
#                         ),
#                         id="modal-example"
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Accordions 페이지
# @app.get("/accordions")
# def accordions():
#     return Html(
#         Head(
#             Title("Accordions • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Accordions"),
#                     Details(
#                         Summary("Accordion 1"),
#                         P("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
#                     ),
#                     Details(
#                         Summary("Accordion 2"),
#                         Ul(
#                             Li("Vestibulum id elit quis massa interdum sodales."),
#                             Li("Nunc quis eros vel odio pretium tincidunt nec quis neque."),
#                             Li("Quisque sed eros non eros ornare elementum."),
#                             Li("Cras sed libero aliquet, porta dolor quis, dapibus ipsum.")
#                         ),
#                         open=True
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Article 페이지
# @app.get("/article")
# def article():
#     return Html(
#         Head(
#             Title("Article • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Article(
#                     H2("Article"),
#                     P("Nullam dui arcu, malesuada et sodales eu, efficitur vitae dolor."),
#                     Footer(Small("Duis nec elit placerat, suscipit nibh quis, finibus neque.")),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Group 페이지
# @app.get("/group")
# def group():
#     return Html(
#         Head(
#             Title("Group • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Group"),
#                     Form(
#                         Fieldset(
#                             Input(type="email", name="email", placeholder="Enter your email", autocomplete="email"),
#                             Input(type="submit", value="Subscribe"),
#                             role="group"
#                         ),
#                         cls="container"
#                     ),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Progress 페이지
# @app.get("/progress")
# def progress():
#     return Html(
#         Head(
#             Title("Progress • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Progress bar"),
#                     Progress(id="progress-1", value="25", max="100"),
#                     Progress(id="progress-2"),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # Loading 페이지
# @app.get("/loading")
# def loading():
#     return Html(
#         Head(
#             Title("Loading • Pico CSS"),
#             Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css")
#         ),
#         Body(
#             create_header(),
#             Main(
#                 Section(
#                     H2("Loading"),
#                     Article(aria_busy="true"),
#                     Button("Please wait…", aria_busy="true"),
#                     cls="container"
#                 ),
#                 cls="container"
#             ),
#             create_footer()
#         )
#     )

# # 서버 실행
# serve()