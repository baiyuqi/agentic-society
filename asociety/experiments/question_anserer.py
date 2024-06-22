from asociety.generator.persona_skeleton_generator import *
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
from asociety.generator.llm_engine import llm, from_skeleton
with open('prompts/experiment.json') as pjson:
            prompts = json.load(pjson)
            
           
            pjson.close()
output_parser = StrOutputParser()


class QuestionAnwserer:
    def __init__(self, persona, question) -> None:
        self.persona = persona
        self.question = question
            
    def getAnwser(self):
        persona = self.persona['persona_desc']
        question = self.question['question']
        options = self.question['options']
        question_set = self.question['question_set']

        fs = prompts[question_set]["question_prompt"]
        question_prompt = ChatPromptTemplate.from_template(fs)
        chain = question_prompt | llm | output_parser
        anwser = chain.invoke({"persona":persona,"question":question, "options":options })
        
        return anwser
  
class SheetAnwserer:
    def __init__(self, persona) -> None:
        self.persona = persona

            

    def getAnwser(self,sheet, question_set):
        persona = self.persona['persona_desc']
        fs = prompts[question_set]["sheet_prompt"]
        question_prompt = ChatPromptTemplate.from_template(fs)
        pro = question_prompt.invoke({"persona":persona,"sheet":sheet})
        chain = question_prompt | llm | output_parser
        anwser = chain.invoke({"persona":persona,"sheet":sheet})
        
        return anwser
