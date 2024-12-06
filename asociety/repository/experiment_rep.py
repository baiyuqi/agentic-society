from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String,Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from asociety.repository.database import Base

class Question(Base):
    __tablename__ = "question"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    question_set:  Mapped[str] = mapped_column(String(30),nullable=True)
    question:  Mapped[Optional[str]]
    options:  Mapped[Optional[str]]
    answer:  Mapped[Optional[str]]
    other_type:  Mapped[str] = Column("other.type", String(50))
    other_level: Mapped[str] = Column("other.level", String(50))
 
    def __repr__(self) -> str:
        return f"PersonaGroup(id={self.id!r}, name={self.question_set!r}, question={self.question!r}, options={self.options!r}"
class PersonaGroup(Base):
    __tablename__ = "persona_group"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30),nullable=True)
    description: Mapped[str] = mapped_column(String(30),nullable=True)

    personas: Mapped[Optional[str]]
 
    def __repr__(self) -> str:
        return f"PersonaGroup(id={self.id!r}, name={self.name!r}, description={self.description!r}, personas={self.personas!r}"
class QuestionGroup(Base):
    __tablename__ = "question_group"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(30),nullable=True)
    table: Mapped[str] = mapped_column(String(30),nullable=True)
    name: Mapped[str] = mapped_column(String(30),nullable=True)
    question_set: Mapped[str] = mapped_column(String(30),nullable=True)
  
    description: Mapped[str] = mapped_column(String(30),nullable=True)

    questions: Mapped[Optional[str]]
    quiz_sheet: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"QuestionGroup(id={self.id!r}, name={self.name!r}, description={self.description!r},  questions={self.questions!r})"


class ExperimentEntity(Base):
    __tablename__ = "experiment"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30),nullable=True)
    type: Mapped[str] = mapped_column(String(30),nullable=True)
    description: Mapped[str] = mapped_column(String(30),nullable=True)

    persona_group:Mapped[str] =  mapped_column(String(30),nullable=True)
    question_group:Mapped[str] =   mapped_column(String(30),nullable=True)
    def __repr__(self) -> str:
        return f"ExperimentEntity(id={self.id!r}, name={self.name!r}, description={self.description!r}, personas={self.education!r}, questions={self.questions!r})"


class QuestionAnswer(Base):
    __tablename__ = "question_answer"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    index: Mapped[int] =  Column(Integer)
    experiment_name: Mapped[str] = mapped_column(String(30),nullable=True)
    persona_id: Mapped[str] = mapped_column(String(30),nullable=True)
    question_id: Mapped[str] = mapped_column(String(30),nullable=True)
    agent_answer: Mapped[Optional[str]]
    agent_solution: Mapped[Optional[str]]
    response: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"QuestionAnswer(id={self.id!r}, experiment_name={self.experiment_name!r}, persona_id={self.persona_id!r}, question={self.question!r}, anwser={self.agent_answer!r})"
    

class QuizAnswer(Base):
    __tablename__ = "quiz_answer"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    index: Mapped[int] =  Column(Integer)
    experiment_name: Mapped[str] = mapped_column(String(30),nullable=True)
    persona_id: Mapped[str] = mapped_column(String(30),nullable=True)
    agent_answer: Mapped[Optional[str]]
    response: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"QuestionAnswer(id={self.id!r}, experiment_name={self.experiment_name!r}, persona_id={self.persona_id!r}, question_group_id={self.question_group_id!r}, anwser={self.agent_answer!r})"

class QuestionAnswerSummary(Base):
    __tablename__ = "question_answer_summary"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    experiment_name: Mapped[str] = mapped_column(String(30),nullable=True)
    persona_id: Mapped[str] = mapped_column(String(30),nullable=True)
    score: Mapped[float] = Column(Float)
 
    def __repr__(self) -> str:
        return f"QuestionAnswer(id={self.id!r}, experiment_name={self.experiment_name!r}, persona_id={self.persona_id!r}, score={self.score!r})"

if __name__ == "__main__":
    import asociety.repository.database as db
    Base.metadata.create_all(db.engine)