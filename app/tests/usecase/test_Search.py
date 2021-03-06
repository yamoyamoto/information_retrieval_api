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


def testTfIdf(pre_function):
    action = SearchDocumentAction()
    result = action.byTFIdf("揚げ")

    assert len(result) == 1
    # 川口 友也 は 唐 揚げ が 大好き です 。
    idf_expected = math.log(3/1)
    assert result[0].tf == 1/9
    assert result[0].tfIdf == 1/9 * idf_expected

    result = action.byTFIdf("川口")
    assert len(result) == 3
    assert result[0].document.body == "川口友也は大阪生まれ、大阪出身です。"
    assert result[1].document.body == "川口友也は唐揚げが大好きです。"
    assert result[2].document.body == "川口友也は大阪市立大学に通っています。"

    idf_expected = math.log(3/3)
    assert result[2].tf == 1/10
    assert result[2].tfIdf == 1/10 * idf_expected

    result = action.byTFIdf("大阪")
    assert len(result) == 1
    result[0].document.body == "川口友也は大阪生まれ、大阪出身です。"
    idf_expected = math.log(3/1)

    assert result[0].tf == 2/9
    assert result[0].tfIdf == 2/9 * idf_expected
