from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String,Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass
class Personality(Base):
    __tablename__ = "personality"
    persona_id: Mapped[int] =  Column(Integer, primary_key=True)
    model:Mapped[str] = mapped_column(String(30),nullable=True)
    theory:  Mapped[str] = mapped_column(String(30),nullable=True)
    question: Mapped[int] =  Column(Integer)
    personality_json: Mapped[Optional[str]]


    extraversion:  Mapped[float] = Column(Float)
    friendliness:  Mapped[float] = Column(Float) 
    gregariousness:  Mapped[float] = Column(Float)
    assertiveness:  Mapped[float] = Column(Float)
    activity_level:  Mapped[float] = Column(Float)
    excitement_seeking:  Mapped[float] = Column(Float)
    cheerfulness:  Mapped[float] = Column(Float)

    agreeableness:  Mapped[float] = Column(Float)
    trust:  Mapped[float] = Column(Float)
    morality:  Mapped[float] = Column(Float)
    altruism:  Mapped[float] = Column(Float)
    cooperation:  Mapped[float] = Column(Float)
    modesty:  Mapped[float] = Column(Float)
    sympathy:  Mapped[float] = Column(Float)

    conscientiousness:  Mapped[float] = Column(Float)
    self_efficacy:  Mapped[float] = Column(Float)
    orderliness:  Mapped[float] = Column(Float)
    dutifulness:  Mapped[float] = Column(Float)
    achievement_striving:  Mapped[float] = Column(Float)
    self_discipline:  Mapped[float] = Column(Float)
    cautiousness:  Mapped[float] = Column(Float) 

    neuroticism:  Mapped[float] = Column(Float)
    anxiety:  Mapped[float] = Column(Float)
    anger:  Mapped[float] = Column(Float)
    depression:  Mapped[float] = Column(Float)
    self_consciousness:  Mapped[float] = Column(Float)
    immoderation:  Mapped[float] = Column(Float)
    vulnerability:  Mapped[float] = Column(Float) 

    openness:  Mapped[float] = Column(Float)
    imagination:  Mapped[float] = Column(Float)
    artistic_interests:  Mapped[float] = Column(Float)
    emotionality:  Mapped[float] = Column(Float)
    adventurousness:  Mapped[float] = Column(Float)
    intellect:  Mapped[float] = Column(Float)
    liberalism:  Mapped[float] = Column(Float) 

    extraversion_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    friendliness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    gregariousness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    assertiveness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    activity_level_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    excitement_seeking_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    cheerfulness_score:  Mapped[str] = mapped_column(String(30),nullable=True)

    agreeableness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    trust_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    morality_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    altruism_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    cooperation_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    modesty_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    sympathy_score:  Mapped[str] = mapped_column(String(30),nullable=True)

    conscientiousness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    self_efficacy_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    orderliness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    dutifulness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    achievement_striving_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    self_discipline_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    cautiousness_score:  Mapped[str] = mapped_column(String(30),nullable=True) 

    neuroticism_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    anxiety_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    anger_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    depression_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    self_consciousness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    immoderation_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    vulnerability_score:  Mapped[str] = mapped_column(String(30),nullable=True) 

    openness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    imagination_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    artistic_interests_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    emotionality_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    adventurousness_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    intellect_score:  Mapped[str] = mapped_column(String(30),nullable=True)
    liberalism_score:  Mapped[str] = mapped_column(String(30),nullable=True)
 
    def __repr__(self) -> str:
        return f"Personality(persona_id={self.persona_id!r}, extraversion={self.extraversion!r}, agreeableness={self.agreeableness!r}, conscientiousness={self.conscientiousness!r}"
def savePersonalities(ps):
    from asociety.repository.database import engine
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        for p in ps:
            session.add(p)
        session.commit()
if __name__ == "__main__":
    import asociety.repository.database as db
    Base.metadata.create_all(db.engine)