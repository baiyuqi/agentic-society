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
def curve_dist(c1, c2):
    sum = 0
    for i in range(len(c1)):
        d = c1[i] - c2[i]
        d2 = d * d
        sum +=d2
    import math
    result = math.sqrt(sum/len(c1))
    return result

if __name__ == "__main__": 
    llm = llm_mean_age()
    real_bhps = real_mean_age('BHPS')
    rea_gsoep = real_mean_age('GSOEP')
    inter = intersection(llm, real_bhps)



    real_bhps = align(real_bhps, inter)
    rea_gsoep = align(rea_gsoep, inter)
    llm = align(llm, inter)
    print(llm)
    llm.to_csv('data/cross_section/llm_glm4.csv')

    import numpy as np
    bigfive = ['extraversion','agreeableness','conscientiousness','neuroticism','openness']
    dist_real = []
    dist_bhps = []
    dist_gsoep = []
    for bf in bigfive:
        ex1 = real_bhps[bf].to_numpy()
        ex2 = rea_gsoep[bf].to_numpy()
        ex3 = llm[bf].to_numpy()

        dist = curve_dist(ex1, ex2)
        dist = round(dist, 2)
        dist1 = curve_dist(ex1, ex3)
        dist1 = round(dist1, 2)
    
        dist2 = curve_dist(ex2, ex3)
        dist2 = round(dist2, 2)
        dist_real.append(dist)
        dist_bhps.append(dist1)
        dist_gsoep.append(dist2)
    distances = pd.DataFrame([dist_real, dist_bhps, dist_gsoep],columns=bigfive)
    distances.to_csv('data/cross_section/distances.csv')
    print(distances)
