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
def align(data, inter):

    data = data.loc[data['age_range'].isin(inter)]
  
    return data
def intersection(real, llm):
    rrange = set(real['age_range'].to_numpy())

    print(rrange)
    lrange = set(llm['age_range'].to_numpy())
    inter = rrange.intersection(lrange)
    return inter



def llm_mean_age():
    sql = '''select age_range,count(*) as sample_size,AVG(extraversion) as extraversion,AVG(agreeableness) as agreeableness,AVG(conscientiousness) as conscientiousness,AVG(neuroticism) as neuroticism,AVG(openness) as openness from persona_personality GROUP BY age_range '''

   
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
    real_bhps = real_mean_age('BHPS')
    rea_gsoep = real_mean_age('GSOEP')
    inter = intersection(llm, real_bhps)



    real_bhps = align(real_bhps, inter)
    rea_gsoep = align(rea_gsoep, inter)
    llm = align(llm, inter)

    import numpy as np
    ex1 = real_bhps['extraversion'].to_numpy()
    ex2 = rea_gsoep['extraversion'].to_numpy()
    ex3 = llm['extraversion'].to_numpy()

    dist = np.linalg.norm(ex1 - ex2)
    dist1 = np.linalg.norm(ex1 - ex3)
    print(dist)