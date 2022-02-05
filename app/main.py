from array import array
from fastapi import FastAPI
import MeCab
from pydantic import BaseModel

from models import MecabWord, MecabSentence


class Query(BaseModel):
    text: str = None
    use_word_class_filter: bool = False
    word_classes = []


app = FastAPI()


@app.post("/")
def root(query: Query):
    reqBody = query.dict()
    text = reqBody["text"]
    useFilter = reqBody["use_word_class_filter"]
    wordClasses = reqBody["word_classes"]

    mecab = MeCab.Tagger()
    node = mecab.parseToNode(text)

    wakati = []
    mecabSentence = MecabSentence()
    while node:
        if node.surface != "":
            wakati.append(node.surface)
            mecabWord = MecabWord(node.surface)
            mecabWord.parseFeatureString(node.feature)
            mecabSentence.add(mecabWord)
        node = node.next

    if useFilter:
        mecabSentence.filter(wordClasses)

    mecabWords = mecabSentence.sortByWordCount()

    return {"message": "Hello World!", "mecabWords": mecabWords, "surfaces": wakati}
