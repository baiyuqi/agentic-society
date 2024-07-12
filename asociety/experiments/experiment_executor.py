import pandas as pd
from asociety.experiments.question_anserer import QuestionAnwserer,SheetAnwserer
from asociety.repository.database import engine
class ExperimentExecutor:
    def __init__(self) -> None:
        pass
    def executeExperiment(self, name,type, persist):
        from asociety.utils import question_set_by_experiment_name
        question_set = question_set_by_experiment_name(name)
        if(type == 'quiz_sheet'):
            self.executeQuizSheet(name=name, persist=persist, question_set=question_set)
        else:
            self.executeByquestion(name=name, persist=persist, question_set=question_set)
    def executeQuizSheet(self, name, persist,question_set):
        from asociety.utils import question_set_by_experiment_name
        question_set = question_set_by_experiment_name(name)
        sql = "SELECT * from quiz_answer where experiment_name = '" + name + "' and agent_answer IS NULL "
        df = pd.read_sql_query(sql, engine)
        if df.empty:
            import tkinter.messagebox as mbox
            mbox.showinfo('no task to execute!','no task to execute!')
            return
        result = []
        for i, row in df.iterrows():
            id = row['id']
            persona_id = row['persona_id']
           
            persona = pd.read_sql_query("select * from persona where id = " + str(persona_id) + "", engine).iloc[0]
            sheet = row['quiz_sheet']
            exe: SheetAnwserer = SheetAnwserer(persona)
            resp = exe.getAnwser(sheet,question_set)
          
            rec = {'id':id, 'type':'quiz_sheet', 'persona_id':persona_id, 'response':resp}
            persist(rec)
            result.append(rec)

        return result
    def executeByquestion(self, name, persist,question_set):
        sql = "SELECT * from question_answer where experiment_name = '" + name + "' and agent_answer IS NULL "

        df = pd.read_sql_query(sql, engine)
        if df.empty:
            import tkinter.messagebox as mbox
            mbox.showinfo('no task to execute!','no task to execute!')        
            return
        result = []
        for i, row in df.iterrows():
            id = row['id']
            persona_id = row['persona_id']
            question_id = row['question_id']
            persona = pd.read_sql_query("select * from persona where id = " + str(persona_id) + "", engine).iloc[0]
            question = pd.read_sql_query("select * from question where id = " + str(question_id) + "", engine).iloc[0]
            exe: QuestionAnwserer = QuestionAnwserer(persona, question)
            #resp = exe.getAnwser(question_set)
            answer, solution, resp = 'answer', 'solution', 'response'#self.parse(resp)
            rec = {'id':id, 'type':'by_question', 'persona_id':persona_id, 'question_id':question_id, 'answer':answer, 'solution':solution, 'response':resp}
            persist(rec)
            result.append(rec)

        return result
    def parse(self,mas):
        resp = mas
        try:

            if(mas.startswith('```')):
                mas = mas.split("```")
                mas = mas[1]
                mas = mas.split("json\n")
                mas = mas[1]
            mas = mas.replace("\\","\\\\")

            import json
            mjason = json.loads(mas)
            answer = mjason['answer']
            solution = mjason['solution']
            return answer, solution,resp

        except:
            return "", "", resp
            
        

if __name__ == "__main__":
    str = '''
Based on the persona you've described, here's how the answers to the Big Five personality test questions might look in JSON format. Please note that these answers are hypothetical and based on the typical characteristics one might expect from a middle-aged professional with a stable career and family life:

```json
[
  {"question_id": 1, "answer": 2}, // Moderately Inaccurate - Worry about things.
  {"question_id": 2, "answer": 4}, // Moderately Accurate - Make friends easily.
  {"question_id": 3, "answer": 3}, // Neither Accurate Nor Inaccurate - Have a vivid imagination.
  {"question_id": 4, "answer": 4}, // Moderately Accurate - Trust others.
  {"question_id": 5, "answer": 5}, // Very Accurate - Complete tasks successfully.
  {"question_id": 6, "answer": 1}, // Very Inaccurate - Get angry easily.
  {"question_id": 7, "answer": 2}, // Moderately Inaccurate - Love large parties.
  {"question_id": 8, "answer": 4}, // Moderately Accurate - Believe in the importance of art.
  {"question_id": 9, "answer": 1}, // Very Inaccurate - Use others for my own ends.
  {"question_id": 10, "answer": 4}, // Moderately Accurate - Like to tidy up.
  {"question_id": 11, "answer": 2}, // Moderately Inaccurate - Often feel blue.
  {"question_id": 12, "answer": 4}, // Moderately Accurate - Take charge.
  {"question_id": 13, "answer": 3}, // Neither Accurate Nor Inaccurate - Experience my emotions intensely.
  {"question_id": 14, "answer": 4}, // Moderately Accurate - Love to help others.
  {"question_id": 15, "answer": 5}, // Very Accurate - Keep my promises.
  {"question_id": 16, "answer": 2}, // Moderately Inaccurate - Find it difficult to approach others.
  {"question_id": 17, "answer": 5}, // Very Accurate - Am always busy.
  {"question_id": 18, "answer": 2}, // Moderately Inaccurate - Prefer variety to routine.
  {"question_id": 19, "answer": 1}, // Very Inaccurate - Love a good fight.
  {"question_id": 20, "answer": 5}  // Very Accurate - Work hard.
]
```

'''
    import re

   
    rs = re.findall(r"\{(.*?)\}",str)
    rs = ['{' + e + '}' for e in rs]
    json = ','.join(rs)
    print(json)