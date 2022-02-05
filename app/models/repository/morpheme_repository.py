import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from app.models.entity.Morpheme import Morpheme

engine = sqlalchemy.create_engine('sqlite:////app/ir_db.db', echo=True)
Base = declarative_base()


class MorphemeRepository(Base):
    __tablename__: str = "term"
    id = Column(Integer, primary_key=True)
    body = Column(String(length=255))
    idf = Column(Integer)

    def __init__(self) -> None:
        pass

    def save(self, morpheme: Morpheme):
        session = sessionmaker(bind=engine)()
        # self.id
        self.body = morpheme.surface
        session.add(instance=morpheme)
        session.commit()


Base.metadata.create_all(bind=engine)
