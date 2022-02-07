from app.models.entity.Document import Document

from app.models.entity.Term import Term


args = {
    "surface": "川口",
    "document_body": "川口友也は大阪出身です。",
    "document_id": 1,
    "tf": 1,
    "df": 7,
}


def test_Initialize():

    term = Term(args)
    assert term.surface == "川口"
    assert isinstance(term.document, Document)
    assert term.tf == 1
    assert term.df == 7
    # log(7/7)
    assert term.tfIdf == 0


def test_InitializeWhenInvalidDf():
    invalidArgs = args
    invalidArgs["df"] = 0
    invalidArgs["tf"] = 2

    term = Term(args)
    assert term.idf == 100000
    assert term.tfIdf == 200000
