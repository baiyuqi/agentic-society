from asociety.generator.persona_skeleton_generator import *
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
from asociety.generator.llm_engine import llm, from_skeleton

output_parser = StrOutputParser()
chain = from_skeleton | llm | output_parser
class PersonaGenerator:
    def __init__(self) -> None:

        self.skeletonGenerator = PersonaSkeletonGeneratorFactory.create()
        self.enricher = chain
            
    def sampling(self, n):
        ssamples = self.skeletonGenerator.sampling(n)
        rst = []
        for index, skel in ssamples.iterrows():
            obj = {}
            keys = skel.keys();

            for key in keys:
                 if(key in ["fnlwgt","probability"]):
                      continue
                 obj[key] = skel[key]
                 
            rst.append(self.llm_enrich(obj))
        return rst
    def llm_enrich(self, skel):
        persona = json.dumps(skel)
        enriched = self.enricher.invoke({persona})
        skel["persona_desc"] = enriched;
        return skel
class PersonaGeneratorFactory:
    def create():
        return PersonaGenerator()
