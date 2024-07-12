from asociety.repository.database import engine

def data(ps):
        result = [[],[],[],[],[],[]]
        
        for i, r in enumerate(ps):
            for j in range(0, 6):
                result[j].append(r[j])
 
        return result

def compute(age, d):        
        import numpy as np
        x = np.array(age)
        y = np.array(d)

        z = np.polyfit(x, y, 3)
        p = np.poly1d(z)
        yvals = p(x)
        return x, y, yvals

def get_personas_ana():
    from sqlalchemy.orm import Session
    from sqlalchemy import text
    with Session(engine) as session:
        ps = session.execute(text('select age,openness ,conscientiousness ,extraversion, agreeableness, neuroticism  FROM persona_personality where sex = "Male" ORDER BY age '))
        title = ['openness' ,'conscientiousness' ,'extraversion', 'agreeableness', 'neuroticism']
        import matplotlib.pyplot as plt
        import matplotlib
        import numpy as np
        mdata = data(ps)
 
        return mdata

      
   

