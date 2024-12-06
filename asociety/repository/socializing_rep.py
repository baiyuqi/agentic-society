
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

from sqlalchemy import Column, Integer, String
from asociety.repository.database import Base
class Chat(Base):
    __tablename__ = "chat"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    chatters: Mapped[str] 
    state: Mapped[str] 
    summary: Mapped[str] 

    def __repr__(self) -> str:
        return f"Persona(id={self.id!r}, chatters={self.chatters!r}, state={self.state!r}, education={self.summary!r})"

class FriendRelationship(Base):
    __tablename__ = "friend_relationship"
    from_id: Mapped[int] =  Column(Integer, primary_key=True)
    to_id: Mapped[int] =  Column(Integer, primary_key=True)
    
 
    def __repr__(self) -> str:
        return f"FriendRelationship(id={self.id!r}, from_id={self.from_id!r}, to_id={self.to_id!r}"


if __name__ == "__main__":
    import asociety.repository.database as db
    Base.metadata.create_all(db.engine)