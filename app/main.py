from array import array
from fastapi import FastAPI
import MeCab
from pydantic import BaseModel

from models import MecabWord, MecabWordWrapper


class Query(BaseModel):
    text: str = None
    use_word_class_filter: bool = False
    word_classes = []


app = FastAPI()


@app.post("/")
def root(query: Query):
    reqBody = query.dict()
    text = reqBody["text"]
    print(reqBody)
    useFilter = reqBody["use_word_class_filter"]
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

    if useFilter:
        mecabWordCounter.filter(wordClasses)

    mecabWords = mecabWordCounter.sort()

    return {"message": "Hello World!", "mecabWords": mecabWords}
