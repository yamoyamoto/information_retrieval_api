import sqlite3
import pytest
import os

from app.usecase.document.Search import SearchDocumentAction
from app.models.repository.DocumentRepository import DocumentRepository


@pytest.fixture
def pre_function():
    conn = sqlite3.connect(os.environ["DB_PATH"])
    c = conn.cursor()
    c.execute(
        """
        DELETE FROM document;
        """
    )
    c.execute(
        """
        DELETE FROM term_to_document;
        """
    )
    conn.commit()
    conn.close()

    yield "Tear Down"

    conn = sqlite3.connect(os.environ["DB_PATH"])
    c = conn.cursor()
    c.execute(
        """
        DELETE FROM document;
        """
    )
    c.execute(
        """
        DELETE FROM term_to_document;
        """
    )
    conn.commit()
    conn.close()


def testTfIdf(pre_function):
    conn = sqlite3.connect(os.environ["DB_PATH"])
    c = conn.cursor()
    c.execute(
        "INSERT INTO document(id, body) VALUES (1, '川口友也は大阪生まれ、大阪出身です。');"
    )
    c.execute(
        "INSERT INTO document(id, body) VALUES (2, '川口友也は唐揚げが大好きです。');"
    )
    c.execute(
        "INSERT INTO document (id, body) VALUES (3, '川口友也は大阪市立大学に通っています。');"
    )
    conn.commit()
    conn.close()

    # 単語に分ける
    exec(open("/app/app/scripts/seed.py").read())

    repo = DocumentRepository()
    res = repo.getAll()
    print("documentの数は、", len(res))

    action = SearchDocumentAction()
    result = action.byTFIdf("揚げ")

    # for i in range(len(result)):
    #     print(result[i].document.id)

    assert len(result) == 1
