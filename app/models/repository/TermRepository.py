import sqlite3
import os
from typing import List

from app.models.entity.Term import Term


class TermRepository:
    def __init__(self) -> None:
        pass

    def toObj(self, tuple) -> Term:
        term = Term(
            {"surface": tuple[0], "tf": tuple[1], "document_id": tuple[2], "df": tuple[3]})
        return term

    def getBySurface(self, surface: str) -> List[Term]:
        conn = sqlite3.connect(os.environ["DB_PATH"])
        c = conn.cursor()
        c.execute("""SELECT term, tf, document_id FROM term_to_document
            WHERE term=? ;""", (surface,))
        tuples = c.fetchall()

        c.execute("""SELECT SUM(tf) as df FROM term_to_document
            WHERE term=? GROUP BY term;""", (surface,))
        statistics = c.fetchone()
        conn.commit()
        conn.close()

        return list(map(lambda x: self.toObj(x+statistics), tuples))
