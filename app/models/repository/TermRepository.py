import sqlite3
import os
from typing import List

from app.models.entity.Term import Term


class TermRepository:
    def __init__(self) -> None:
        pass

    def toObj(self, tuple) -> Term:
        term = Term(
            {"surface": tuple[0], "tf": tuple[1], "document_id": tuple[2], "document_body": tuple
             [3], "df": tuple[4], "N": tuple[5], })
        return term

    def getBySurface(self, surface: str) -> List[Term]:
        conn = sqlite3.connect(os.environ["DB_PATH"])
        c = conn.cursor()
        c.execute("""SELECT a.term, a.tf, a.document_id, b.body FROM term_to_document a
            LEFT JOIN document b ON a.document_id=b.id
            WHERE term=? ;""", (surface,))
        tuples = c.fetchall()

        c.execute("""SELECT SUM(tf) as df FROM term_to_document
            WHERE term=? GROUP BY term;""", (surface,))
        statistics = c.fetchone()

        c.execute("SELECT COUNT(*) N FROM document")
        all_document_count = c.fetchone()

        conn.commit()
        conn.close()

        return list(map(lambda x: self.toObj(x+statistics+all_document_count), tuples))
