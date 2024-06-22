from asociety.repository.database import engine
from asociety.repository.experiment_rep import QuizAnswer
from asociety.repository.persina_rep import Persona
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
def extract_personas_of_experiment():
    from sqlalchemy.orm import Session
    from sqlalchemy import text
    with Session(engine) as session:
        ps = session.execute(text('select age,openness ,conscientiousness ,extraversion, agreeableness, neuroticism  FROM persona_personality where sex = "Male" ORDER BY age '))
        title = ['openness' ,'conscientiousness' ,'extraversion', 'agreeableness', 'neuroticism']
        import matplotlib.pyplot as plt
        import matplotlib.pyplot as plt
        import numpy as np
        mdata = data(ps)

        fig, axs = plt.subplots(2, 3)
        for i in range(0, 5):
            x, y,yvals = compute(mdata[0],mdata[i + 1])


            row = int(i / 3)
            col = i % 3

            #axs[row, col].set_ylim([0, 100])
            axs[row, col].plot(x, y, '*')
            axs[row, col].plot(x,yvals,'r')
            axs[row, col].set_title(title[i])
        axs[1,2].set_axis_off()    
        for ax in axs.flat:
            ax.set(xlabel='age', ylabel='score')
        fig.tight_layout()
        

        plt.show()
   


 
  
     
if __name__ == "__main__": 
   extract_personas_of_experiment()
