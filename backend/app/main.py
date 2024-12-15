from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

openai_model = ChatOpenAI(model="gpt-4o")
anthropic_model = ChatAnthropic(model_name="claude-3-haiku-20240307")

@app.get("/")
def read_root():
    return {"Hello": "World"}

add_routes(
    app,
    openai_model,
    path="/openai",
)

add_routes(
    app,
    anthropic_model,
    path="/anthropic",
)

joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "ジョークの内容だけを出力してください。前置きは不要です。"),
    ("user", "{topic}に関するジョークを1つ言ってください。")
])
add_routes(
    app,
    joke_prompt | anthropic_model,
    path="/joke",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
