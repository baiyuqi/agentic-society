import pandas as pd
import numpy as np
from typing import List,Dict
class PersonaSkeletonGenerator:
    def __init__(self, df) -> None:
        self.df = df
        self.total = df["fnlwgt"].sum();
        df["probability"] = df["fnlwgt"].apply(lambda x: x/self.total)
        one = df["probability"].sum()
        assert(one == 1)
    def sampling(self,  n:int):
        probs = self.df["probability"]
        probs = [x for x in probs.values]
       
        ser = np.random.choice(self.df.shape[0], n, probs)
       
        samples = self.df.iloc[ser]
        return samples
      
    def enum(self,  column:str):
        values = self.df[column].unique()
        return values
    def margin(self,  column:str):
        values = self.df.groupby(column, sort=False)["probability"].sum().reset_index(name ='probability')
        return values


class PersonaSkeletonGeneratorFactory:
    @classmethod
    def create(cls, column : str = None, value: any = None)-> PersonaSkeletonGenerator:
        df = pd.read_csv('data/census.csv')
        if(column != None):
            df = df[df[column].isin([value])]
        return PersonaSkeletonGenerator(df)
if __name__ == "__main__":
    #df = df[df["occupation"].isin(['Sales'])]
    generator = PersonaSkeletonGeneratorFactory.create()
    margin = generator.enum("occupation")
    samples = generator.sampling(10)


