from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DocumentRepository(Base):
    __tablename__: str = "document"
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    length = Column(Integer)
