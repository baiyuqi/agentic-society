
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass
class FriendRelationship(Base):
    __tablename__ = "friend_relationship"
    id: Mapped[int] =  Column(Integer, primary_key=True, autoincrement=True)
    from_id: Mapped[int] =  Column(Integer)
    to_id: Mapped[int] =  Column(Integer)
    
 
    def __repr__(self) -> str:
        return f"FriendRelationship(id={self.id!r}, from_id={self.from_id!r}, to_id={self.to_id!r}"


if __name__ == "__main__":
    import asociety.repository.database as db
    Base.metadata.create_all(db.engine)