import pandas as pd

def real_mean_age():
    mdf = pd.read_csv('data/cross_section/age_mean.csv')
    s_array = mdf[mdf.columns[2:4]].to_numpy()
    import numpy as np
    pc = np.corrcoef(s_array)
    print(pc)
def real_mean_variation():
    vdf = pd.read_csv('data/cross_section/age_variation.csv')

def llm_mean_age():
    sql = '''select age_range,count(*),AVG(extraversion),AVG(agreeableness),AVG(conscientiousness),AVG(neuroticism),AVG(openness)  from persona_personality GROUP BY age_range '''
    from asociety.repository.database import engine
    from sqlalchemy import text
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        ps = session.execute(text(sql))
        for i, r in enumerate(ps):
            tupe = r.tuple()
            tupe = list(tupe[2:])
            pass
if __name__ == "__main__": 
    llm_mean_age()