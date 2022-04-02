import sqlite3
import os
from typing import List
from app.models.entity.Term import Term, TermCorrection


class TermRepository:
    def __init__(self) -> None:
        pass

    def toObj(self, tuple) -> Term:
        term = Term(
            {"surface": tuple[0], "tf": tuple[1], "document_id": tuple[2], "document_body": tuple
             [3], "df": tuple[6], "document_count": tuple[7], "id": tuple[4], "tf_idf": tuple[5]})
        return term

    def getBySurface(self, surface: str) -> List[Term]:
        conn = sqlite3.connect(os.environ["DB_PATH"])
        c = conn.cursor()
        c.execute("""SELECT a.term, a.tf, a.document_id, b.body, a.id, a.tf_idf FROM term_to_document a
            LEFT JOIN document b ON a.document_id=b.id
            WHERE term=? ;""", (surface,))
        tuples = c.fetchall()

        c.execute("""SELECT COUNT(*) as df FROM term_to_document
            WHERE term=? GROUP BY term;""", (surface,))
        statistics = c.fetchone()

        c.execute("SELECT COUNT(*) as all_document_count FROM document")
        all_document_count = c.fetchone()

        conn.commit()
        conn.close()

        return list(map(lambda x: self.toObj(x+statistics+all_document_count), tuples))

    def fetchNormById(self, documentId: str):
        conn = sqlite3.connect(os.environ["DB_PATH"])
        c = conn.cursor()
        c.execute("""SELECT SUM(tf_idf * tf_idf) as norm 
            FROM term_to_document
            WHERE document_id = ?
            GROUP BY document_id
        """, (documentId,))
        res = c.fetchone()
        return res[0]


def buildTermCorrection(terms: List[Term]) -> TermCorrection:
    return TermCorrection(terms)
