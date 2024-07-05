
from tkinter import *
from tkinter import ttk
from pandastable import Table

import pandas as pd

from asociety.generator.persona_generator import *
class ExperimentExecutorPanel:
    def __init__(self, root) -> None:
        import tkinter as tk
        self.experiment = None
       
            
        self.main = inner_panedwindow = ttk.PanedWindow(root, orient=VERTICAL)
        #inner_panedwindow.pack(fill=BOTH, expand=True)

        # Create two frames to be added to the inner PanedWindow
        top_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')
        bottom_frame = ttk.Frame(inner_panedwindow, width=400, height=200, relief=SUNKEN,style='TFrame')

        # Add the frames to the inner PanedWindow
        inner_panedwindow.add(top_frame, weight=1)
        inner_panedwindow.add(bottom_frame, weight=1)
        self.table = Table(bottom_frame, showtoolbar=True, showstatusbar=True)
        self.table.show()
    
       


        # Label for Entry
        self.name_label = Label(top_frame, text="Enter Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.name_var = StringVar()
        self.name_entry = ttk.Entry(top_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Label for Entry
        self.desc_label = Label(top_frame, text="Enter Description:")
        self.desc_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        # Entry
        self.desc_var = StringVar()
        self.desc_entry = ttk.Entry(top_frame, textvariable=self.desc_var)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.submit_button = ttk.Button(top_frame, text="execute", command=self.execute,style='TButton')
        self.submit_button.grid(row=2, column=0, columnspan=1, pady=10)

        self.submit_button = ttk.Button(top_frame, text="reparse", command=self.reparse,style='TButton')
        self.submit_button.grid(row=2, column=2, columnspan=1, pady=10)       
    def setData(self, ename, updateTree):
        
        from asociety.repository.database import engine
        from sqlalchemy.orm import Session
        from asociety.repository.experiment_rep import ExperimentEntity
        with Session(engine) as session:
            self.experiment = session.query(ExperimentEntity).filter(ExperimentEntity.name==ename).first()
            if(self.experiment.type == 'by_question'):
                df = pd.read_sql_query("select * from question_answer where experiment_name = '" + ename + "'", engine)
            else:
                df = pd.read_sql_query("select * from quiz_answer where experiment_name = '" + ename + "'", engine)
            self.table.model.df = df
            self.table.redraw()
        self.name_var.set(self.experiment.name)
        self.desc_var.set(self.experiment.description)
            
    def execute(self):
        from asociety.experiments.experiment_executor import ExperimentExecutor
        exe = ExperimentExecutor()
        result = exe.executeExperiment(self.experiment.name,self.experiment.type,self.persist)

    def reparse(self):
        df = self.table.model.df
        ind = df.loc[df.agent_answer.isnull()]
        ind = ind.loc[df.response != '']

        for i, row in ind.iterrows():
            id = row['id']
            response = row['response']
            import re
            rs = re.findall(r"\{(.*?)\}",response)
            rs = ['{' + e + '}' for e in rs]
            if(len(rs) == 0):
                print(rs)
            jsons = ','.join(rs)
            jsons = '[' + jsons + ']'
            print(jsons)

            import json
            mjason = json.loads(jsons)
            df.loc[df.id == id, ['agent_answer']] = [jsons]
            self.persist({'id':id, 'type':self.experiment.type, "answer": jsons, 'response': response})

    def persist(self, record):   
        if(record['type'] =='by_question'):
            self.persist_byquestion(record)
        else:
            self.persist_sheet(record) 
    def persist_byquestion(self, record):
        
        from asociety.repository.database import engine
        from sqlalchemy.orm import Session
        from asociety.repository.experiment_rep import QuestionAnswer
        
        from sqlalchemy import select
        with Session(engine) as session:
          
            qa =  session.execute(select(QuestionAnswer).filter_by(id=record['id'])).scalar_one()
            qa.agent_answer = record['answer']

            qa.response = record['response']
            session.commit()
        df = self.table.model.df
        df.loc[df['id'] == record['id'], ['agent_answer','response']] = [record['answer'],record['response']]
    def persist_sheet(self, record):
        
        from asociety.repository.database import engine
        from sqlalchemy.orm import Session
        from asociety.repository.experiment_rep import QuizAnswer
        
        from sqlalchemy import select
        with Session(engine) as session:
            qa =  session.execute(select(QuizAnswer).filter_by(id=record['id'])).scalar_one()
            if 'answer' in record:
                qa.agent_answer = record['answer']
            qa.response = record['response']
            session.commit()
        df = self.table.model.df
        df.loc[df['id'] == record['id'], ['response']] = [record['response']]
if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({'id' :  [0, 1],'agent_answer' :  ['', 'test2.dat'], 
                                    'response': ['ggggg', '']})
    ind = df.loc[df.agent_answer == '']
    ind = ind.loc[df.response != '']
    for i, row in ind.iterrows():
            id = row['id']
            response = row['response']
           
            df.loc[df.id == id, ['agent_answer','agent_solution']] = ["ans", 'sol']
    print(df)