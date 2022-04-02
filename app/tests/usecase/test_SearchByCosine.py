import sqlite3
import pytest
import os
import math

from app.usecase.document.Search import SearchDocumentAction


@pytest.fixture
def pre_function():
    conn = sqlite3.connect(os.environ["DB_PATH"])
    c = conn.cursor()
    c.execute(
        """
        DELETE FROM document;
        """
    )
    # 川口 友也 は 大阪 生まれ 、 大阪 出身 です 。 (10)
    c.execute(
        "INSERT INTO document(id, body) VALUES (1, '川口友也は大阪生まれ、大阪出身です。');"
    )
    # 川口 友也 は 唐 揚げ が 大好き です 。 (9)
    c.execute(
        "INSERT INTO document(id, body) VALUES (2, '川口友也は唐揚げが大好きです。');"
    )
    # 川口 友也 は 大阪市立大学 に 通っ て い ます 。 (10)
    c.execute(
        "INSERT INTO document (id, body) VALUES (3, '川口友也は大阪市立大学に通っています。');"
    )
    c.execute(
        """
        DELETE FROM term_to_document;
        """
    )
    conn.commit()
    conn.close()
    exec(open("/code/app/scripts/seed.py").read())

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


def testCosine(pre_function):
    action = SearchDocumentAction()
    result = action.byCosine("揚げ")

    assert len(result) == 1
    assert result[0].document.body == "川口友也は唐揚げが大好きです。"

    tfIdfOfQuery = 1/9 * math.log(3/1)
    norm = 0
    # 川口
    norm += pow(1/9 * math.log(3/3), 2)
    # 友也
    norm += pow(1/9 * math.log(3/3), 2)
    # は
    norm += pow(1/9 * math.log(3/3), 2)
    # 唐
    norm += pow(1/9 * math.log(3/1), 2)
    # 揚げ
    norm += pow(1/9 * math.log(3/1), 2)
    # が
    norm += pow(1/9 * math.log(3/1), 2)
    # 大好き
    norm += pow(1/9 * math.log(3/1), 2)
    # です
    norm += pow(1/9 * math.log(3/3), 2)
    # 。
    norm += pow(1/9 * math.log(3/3), 2)

    cosine_expected = tfIdfOfQuery/math.sqrt(norm)
    assert result[0].cosine - cosine_expected < 0.01
