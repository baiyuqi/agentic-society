from asociety.generator.persona_skeleton_generator import *
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
import os

from asociety import config
model = config.configuration['llm']

if model == 'glm-4':
    
    apikey = os.getenv('ZHIPU_APIKEY')
    llm = ChatZhipuAI(
        model="glm-4",
        api_key=apikey,
    )
if model == 'local':
    from langchain_openai import OpenAI
    llm = OpenAI(
        model="gpt-4o",
        api_key=apikey,
    )
if model == 'gpt-4o':
    from langchain_openai import OpenAI
    apikey = os.getenv('OPENAI_APIKEY')
    llm = OpenAI(
        model="glm4-chat-9b",
        openai_api_base = ""
        api_key=apikey,
    )
with open('prompts/generation.json') as pjson:
            d = json.load(pjson)
            fs = d["from_skeleton"]
            from_skeleton = ChatPromptTemplate.from_template(fs)
            fv = d["from_void"]
            from_void = ChatPromptTemplate.from_template(fv)
            big_five_explain = d["big_five_explain"]
            
            pe = d["personality_eliciting"]
            personality_eliciting = ChatPromptTemplate.from_template(pe)
            pjson.close()
with open('prompts/chat.json') as pjson:
            d = json.load(pjson)
            sm = d["summary"]
            
            fr = d["friend"]
            friend = ChatPromptTemplate.from_template(fv)
            pjson.close()
from langchain_core.prompts import  MessagesPlaceholder
summary = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                
               
                fr,
            ),
            MessagesPlaceholder(variable_name="messages"),
            
        ]
    )