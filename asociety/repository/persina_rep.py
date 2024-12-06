from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from asociety.repository.database import Base

class Persona(Base):
    __tablename__ = "persona"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    age: Mapped[int]
    workclass: Mapped[str] = mapped_column(String(30),nullable=True)
    education: Mapped[str] = mapped_column(String(30),nullable=True)
    education_num: Mapped[int]
    marital_status: Mapped[str] = mapped_column(String(30),nullable=True)
   
    occupation: Mapped[str] = mapped_column(String(30),nullable=True)
    relationship: Mapped[str] = mapped_column(String(30),nullable=True)
    race: Mapped[str] = mapped_column(String(30),nullable=True)
    sex: Mapped[str] = mapped_column(String(30),nullable=True)
    capital_gain: Mapped[int]
    capital_loss: Mapped[int]
    hours_per_week: Mapped[int]
    native_country: Mapped[str] = mapped_column(String(30),nullable=True)
    income: Mapped[str] = mapped_column(String(30),nullable=True)

    persona_desc: Mapped[Optional[str]]
    elicited: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"Persona(id={self.id!r}, age={self.age!r}, workclass={self.workclass!r}, education={self.education!r}, education_num={self.education_num!r}, marital_status={self.marital_status!r},  occupation={self.occupation!r}, relationship={self.relationship!r}, race={self.race!r}, sex={self.sex!r}, capital_gain={self.capital_gain!r}, capital_loss={self.capital_loss!r}, hours_per_week={self.hours_per_week!r}, native_country={self.native_country!r}, income={self.income!r}, persona_desc={self.persona_desc!r})"



persona_remained_personality = '''
select persona.* from persona left join personality on persona.id = personality.persona_id where personality.persona_id is null
'''




from asociety.repository.database import engine


def savePersonas( ps):

    
    from sqlalchemy.orm import Session

    with Session(engine) as session:
        for p in ps:
            per = toPersona(p)
            session.add(per)
        
        
        session.commit()
    


def savePersona(self, data):
        
    from sqlalchemy.orm import Session

    with Session(engine) as session:
        per = toPersona(data)
        session.add(per)
        
        
        session.commit()

def toPersona( data):
    per = Persona(
        age = data["age"],
        workclass = data['workclass'],
        education=data["education"],
        education_num=data["education.num"],
        marital_status=data["marital.status"],
        occupation=data["occupation"],
        relationship=data["relationship"],
        race=data["race"],
        sex=data["sex"],
        capital_gain=data["capital.gain"],
        capital_loss=data["capital.loss"],
        hours_per_week=data["hours.per.week"],
        native_country=data["native.country"],
        income=data["income"],
        persona_desc=data["persona_desc"]
        )
    
    return per

if __name__ == "__main__":
    import json
    skel = '{"age": 31, "workclass": "Private", "fnlwgt": 399052, "education": "9th", "education.num": 5, "marital.status": "Married-civ-spouse", "occupation": "Farming-fishing", "relationship": "Wife", "race": "White", "sex": "Female", "capital.gain": 0, "capital.loss": 0, "hours.per.week": 42, "native.country": "United-States", "income": "<=50K", "probability": 6.457806879199508e-05}'
    data = json.loads(skel)

    savePersona(data)
