import pandas as pd
from sqlalchemy import create_engine
from asociety.experiments.experiment_generator import Experiment, ExperimentGenerator
from asociety.repository.experiment_rep import *
from asociety.repository.database import engine
class ExperimentPersistor:
    def __init__(self) -> None:
        pass
    def persistExperiment(self, e:Experiment):


        from sqlalchemy.orm import Session

        with Session(engine) as session:
            ent = ExperimentEntity()
            ent.name = e.name
            ent.description = ""
            ent.questios_set = e.question_set
            ps = [str(row['id']) for i, row in e.personas.iterrows()]
            qs = [str(row['id']) for i, row in e.questions.iterrows()]
            ent.personas =  ','.join(ps)
            ent.questions =  ','.join(qs)
            session.add(ent)
            session.commit()
            
            

        personas = e.personas['id'].to_frame()
        personas = personas.rename(columns = {'id':'persona_id'})
        questions = e.questions['id'].to_frame()
        questions = questions.rename(columns = {'id':'question_id'})
        epr = personas.merge(questions, how='cross')
        print(epr)
        epr.insert(1, 'experiment_name', e.name)
        epr.to_sql(name="question_answer", con=engine,if_exists='append', index=True)

        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    g = ExperimentGenerator("math")
    e = g.generateExperiment('test',1, 1,3)
    persistor = ExperimentPersistor()
    persistor.persistExperiment(e)

