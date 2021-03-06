from array import array
from app.models.entity.Document import Document
from app.models.repository.DocumentRepository import DocumentRepository


def test_toObj():
    repo = DocumentRepository()
    tuple = ("1", "川口友也は大阪生まれ、大阪出身です。")
    obj = repo.toObj(tuple)

    assert isinstance(obj, Document)
    assert obj.id == "1"
    assert obj.body == "川口友也は大阪生まれ、大阪出身です。"
