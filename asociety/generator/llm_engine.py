from asociety.generator.persona_skeleton_generator import *
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
llm = ChatZhipuAI(
    model="glm-4",
    api_key="a075eb3edebc5741d238284820988035.6k1unECbt6xLUxfG",
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