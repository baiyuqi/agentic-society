from asociety.generator.persona_skeleton_generator import *
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
import os
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    
    HumanMessage(
        content="你是谁?"
    )
]

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
        temperature = 0.7,
        model="/data1/glm-4-9b-chat",
        openai_api_key="aaa",
        openai_api_base="http://221.229.101.198:8000/v1"
 
    )

answer = llm.invoke(messages)
print(answer.content)