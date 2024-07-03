from asociety.repository.database import engine
from asociety.repository.experiment_rep import QuizAnswer
from asociety.repository.persina_rep import Persona




def personality_of(persona_id):
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        qas = session.query(QuizAnswer).filter(QuizAnswer.persona_id==persona_id).all()
    all = []
    for qa in qas:
        answer = qa.agent_answer

        import json
        awo = json.loads(answer)
        all += awo
    for i, p in enumerate(all):
        
        del p['question_id']
        p['id_question'] =  i+1
        p['id_select'] = p['answer']
        del p['answer']
    return all

def parse_personality(pobj):

    def _parse_one(personality,  name, data):
        first = name.upper()[0]
        setattr(personality, name,  data[first])
        setattr(personality, name + '_score',  data['score'])
        traits = data['traits']
        for t in traits:
            ks = t.keys()
            tname = list(ks)[1]
            tvalue = t[tname]
            tscore = t['score']
            setattr(personality, tname, tvalue)
            tscore_name = tname + '_score'
            setattr(personality, tscore_name, tscore)
    from asociety.repository.personality_rep import Personality
    ps = pobj['person']['result']['personalities']
    personality = Personality()
    personality.theory = pobj['theory']
    personality.model = pobj['model']
    personality.question = pobj['question']
    import json
    pjson = json.dumps(pobj)
    personality.personality_json = pjson

    for p in ps:
        for key in p.keys():
            
            v = p[key]
            _parse_one(personality,key,v)
    return personality



    
def extract(experiment_name):
    from asociety.repository.dao import extract_personas_of_experiment
    ps = extract_personas_of_experiment(experiment_name)
    personalities = []
    for persona in ps:
        rst = personality_of(persona.id)
        from asociety.personality.ipipneo import IpipNeo

        if persona.sex == 'Male':
            sex = 'M'
        else:
            sex = 'F'

        result = IpipNeo(120).compute(
                    sex=sex, age=persona.age, answers={"answers": rst}, compare=True
                )
        p = parse_personality(result)
        p.persona_id = persona.id
        personalities.append(p)

        
        from asociety.personality.ipipneo.quiz import plot_results
        plot_results(result=result)
    return personalities
def plot_peronality(pid):
    from sqlalchemy.orm import Session
    from asociety.repository.personality_rep import Personality
    with Session(engine) as session:
        ps = session.get(Personality, pid)
        from asociety.personality.ipipneo.quiz import plot_results
        import json
        per = json.loads(ps.personality_json)
        plot_results(result=per)

if __name__ == "__main__": 
    plot_peronality(5)
    #ps = extract('personality-2-exp')
    #savePersonalities(ps)
