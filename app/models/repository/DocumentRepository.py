import sqlite3
import os
from app.models.entity.Document import Document


class DocumentRepository:
    id: int
    body: str
    length: int

    def __init__(self) -> None:
        pass

    def toObj(self, tuple):
        obj = Document(tuple[1])
        obj.setId(tuple[0])
        return obj

    def getAll(self):
        conn = sqlite3.connect(os.environ["DB_PATH"])
        c = conn.cursor()
        c.execute("SELECT * FROM document;")
        documents = c.fetchall()
        conn.commit()
        conn.close()

        return list(map(lambda tuple: self.toObj(tuple), documents))
