from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
output_parser = StrOutputParser()
from langchain_community.chat_models import ChatZhipuAI
llm = ChatZhipuAI(
    model="chatglm_turbo",
    api_key="a075eb3edebc5741d238284820988035.6k1unECbt6xLUxfG",
)
result = llm.invoke("tell me something about love");
chain = prompt | llm | output_parser
pv = prompt.invoke({"topic": "ice cream"})
result = chain.invoke({"topic": "ice cream"})
print(result)