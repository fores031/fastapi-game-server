from sqlalchemy import  Column, Integer, Float, ForeignKey
from sqlachemy.orm import relationship
from database import Base
class Score(Base):
    __tablename__ = "score"

    id        = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer,ForeignKey("users.id"))
    clicks = Column(Integer, default=0)
    gold = Column(Float, default = 0)

user = relationship("user", )
