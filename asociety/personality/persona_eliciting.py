from asociety.repository.database import engine
from asociety.repository.experiment_rep import QuizAnswer
from asociety.repository.personality_rep import Personality
from asociety.repository.persina_rep import Persona
average='''
select AVG(extraversion),AVG(conscientiousness) ,AVG(openness) ,AVG(neuroticism) ,AVG(agreeableness)  FROM personality
'''
big_five_sql = '''
select persona.*, personality.* from personality LEFT JOIN persona on personality.persona_id = persona.id

'''

from asociety.generator.llm_engine import llm, big_five_explain, personality_eliciting
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = personality_eliciting | llm | output_parser
def query_personalities():
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        ps = session.query(Personality).all()
        rst = []
        for p in ps:
            persona = session.query(Persona).get(p.persona_id)
            rst.append({'persona':persona,'personality':p})
        return rst
def big_five(bf:Personality):
    bf = {'extraversion':bf.extraversion_score, 'agreeableness':bf.agreeableness_score,
     'conscientiousness':bf.conscientiousness_score,'neuroticism':bf.neuroticism_score,'openness':bf.openness_score }    
    import json
    bfs = json.dumps(bf)
    return bfs
def elicit(persona:Persona, personality:Personality):
    bfp = big_five(personality)
    elicited = chain.invoke({'persona':persona.persona_desc, 'big_five_explain':big_five_explain, 'big_five_result':bfp})
    print(elicited)
def save_elicited(per:Persona, elicited):
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        session.query(Persona).filter(Persona.id == per.id).update({'elicited': elicited})
        session.commit()  
def elicit_by_id(pid):
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        p =  session.get(Persona, pid)
        per = session.get(Personality, pid)
        elicit(p, per)
if __name__ == "__main__": 
    #ps = extract_personas_of_experiment()
    #for p in ps:
    #   elicited = elicit(p['persona'], p['personality'])
    #    save_elicited(p['persona'], elicited)
    elicit_by_id(5)