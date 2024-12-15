from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langserve import RemoteRunnable

openai = RemoteRunnable("http://localhost:8000/openai")
anthropic = RemoteRunnable("http://localhost:8000/anthropic")
joke = RemoteRunnable("http://localhost:8000/joke")

# # トピックに関するジョークを言ってもらう
# res = joke.invoke({"topic": "猫"})
# print(res.content.strip())

# ジョークを言ってもらう
joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "ジョークの内容だけを出力してください。前置きは不要です。"),
    ("human", "ジョークを1つ言ってください。")
])
joke_chain = joke_prompt | anthropic

# ジョークが面白いかどうかを判定する
judge_prompt = ChatPromptTemplate.from_messages([
    ("system", "ジョークが面白いかどうかを判定してください。"),
    ("human", "{joke}")
])
judge_chain = judge_prompt | openai

chain = {"joke": joke_chain} | RunnablePassthrough.assign(
    judge=judge_chain
)

res = chain.invoke({})
print("ジョーク:")
print(res["joke"].content.strip())
print("判定:")
print(res["judge"].content.strip())
