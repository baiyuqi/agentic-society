import pandas as pd
import numpy as np
from typing import List,Dict
import sqlite3

 
class Selector:

    def selectRandomly(self,  n:int):
        samples = self.df.sample(n)
        return samples
      

    def selectOnColumn(self, col_name, n_per_value:int):
        enum = self.enum(col_name)
        rst  = pd.DataFrame(columns=self.df.columns)
        for e in enum:
            ef = self.df[self.df[col_name] == e]
            samples = ef.sample(n_per_value)
            rst = rst._append(samples)
        
        return rst
    def selectByColumn(self, col_name, col_value, total:int):
        enum = self.enum(col_name)
        type = self.df.dtypes[col_name]
        if type.name == 'int64':
            col_value = int(col_value)
        ef = self.df[self.df[col_name] == col_value]
        samples = ef.sample(total)
        return samples
    def columns(self):
        return self.df.columns
    def enum(self,  column:str):
        values = self.df[column].unique()
        return values
class QuestionSelector(Selector):
    def __init__(self, question_set) -> None:
     
        con = sqlite3.connect("data/db/agentic_society.db")
        sql = "SELECT * from question where question_set = '" + question_set + "'"
        self.df = pd.read_sql_query(sql, con)
        self.question_set = question_set
 
 
class PersonaSelector(Selector):
    def __init__(self) -> None:
        from asociety.repository.database import engine
        
        self.df = pd.read_sql_query("SELECT * from persona", engine)
 
class Experiment:
    def __init__(self, name, question_set, personas, questions) -> None:
        self.name = name
        self.question_set = question_set
        self.personas = personas
        self.questions = questions
    def execute(self):
        pass
