from fastapi import FastAPI
import MeCab
from pydantic import BaseModel

from models import MecabWord, MecabWordWrapper


class Query(BaseModel):
    text: str = None


app = FastAPI()


@app.post("/")
def root(query: Query):
    reqBody = query.dict()
    text = reqBody["text"]
    useFilter = "use_filter" in reqBody
    wordClasses = reqBody["word_classes"] if (
        "word_classes" in reqBody) else []

    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)

    mecabWordCounter = MecabWordWrapper()
    while node:
        mecabWord = MecabWord(node.surface)
        mecabWord.parseFeatureString(node.feature)
        mecabWordCounter.add(mecabWord)
        node = node.next

    mecabWords = mecabWordCounter.sort()

    return {"message": "Hello World!", "mecabWords": mecabWords}
