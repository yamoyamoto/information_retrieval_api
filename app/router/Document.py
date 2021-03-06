from fastapi import APIRouter
from pydantic import BaseModel

from app.usecase.document.Search import SearchDocumentAction

router = APIRouter(
    prefix="/document"
)


@router.get("/")
def showAllDocuments():
    pass


class SearchQuery(BaseModel):
    q: str


@router.post("/search/tf_idf")
def searchByTfIdf(query: SearchQuery):
    reqBody = query.dict()
    q = reqBody["q"]

    actionObj = SearchDocumentAction()
    result = actionObj.byTFIdf(q)
    return {"result": result}


@router.post("/search/cosine")
def searchByCosine(query: SearchQuery):
    reqBody = query.dict()
    q = reqBody["q"]

    actionObj = SearchDocumentAction()
    result = actionObj.byCosine(q)
    return {"result": result}
