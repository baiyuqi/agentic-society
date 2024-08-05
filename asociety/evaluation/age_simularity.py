import pandas as pd

def real_mean_age(section):
    mdf = pd.read_csv('data/cross_section/age_mean_' + section + '.csv')
    return mdf
    #s_array = mdf[mdf.columns[2:4]].to_numpy()
    # import numpy as np
    # pc = np.corrcoef(s_array)
    # print(pc)
def real_mean_variation(section):
    vdf = pd.read_csv('data/cross_section/age_variation_' + section + '.csv')
def align(real, llm):
    rrange = set(real['age_range'].to_numpy())

    print(rrange)
    lrange = set(llm['age_range'].to_numpy())
    inter = rrange.intersection(lrange)
    real = real.loc[real['age_range'].isin(inter)]
    llm = llm.loc[llm['age_range'].isin(inter)]
    return (real, llm)

def llm_mean_age():
    sql = '''select age_range,count(*) as sample_size,AVG(extraversion),AVG(agreeableness),AVG(conscientiousness),AVG(neuroticism),AVG(openness)  from persona_personality GROUP BY age_range '''

   
    from asociety.repository.database import engine
    df = pd.read_sql(sql, engine)
    return df
    # from sqlalchemy import text
    # from sqlalchemy.orm import Session
    # with Session(engine) as session:
    #     ps = session.execute(text(sql))
    #     for i, r in enumerate(ps):
    #         tupe = r.tuple()
    #         tupe = list(tupe[2:])
    #         pass
if __name__ == "__main__": 
    llm = llm_mean_age()
    real = real_mean_age('BHPS')
    align(real, llm)