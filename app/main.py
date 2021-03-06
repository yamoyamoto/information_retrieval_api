from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.models.entity.Document import Document
from app.router import Document as DocumentRouter
from app.usecase.MiniSearchEngine import MiniSearchEngineAction


class Query(BaseModel):
    text: str
    use_word_class_filter: bool = False
    word_classes = []


app = FastAPI()
app.include_router(DocumentRouter.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
def root(query: Query):
    reqBody = query.dict()
    text = reqBody["text"]
    useFilter = reqBody["use_word_class_filter"]
    wordClasses = reqBody["word_classes"]

    document = Document(text)
    document.parseFromString()

    if useFilter:
        document.filterByWordClasses(wordClasses)

    mecabWords = document.sortByWordCount()

    return {"message": "Hello World!", "morphemes": mecabWords, "surfaces": document.wakati}


@app.get("/search")
def search(q: str, start_index: str):
    action = MiniSearchEngineAction()
    items = action.Search(q, start_index)
    return items
