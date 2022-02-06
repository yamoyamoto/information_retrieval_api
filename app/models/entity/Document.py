from app.models.entity.Morpheme import Morpheme, MorphemeCounter
import ipadic
import MeCab

from typing import List


def parse(document: str):
    mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
    node = mecab.parseToNode(document)

    morphemes = []
    while node:
        if node.surface != "":
            tmp = {
                "surface": node.surface,
                "feature": node.feature,
            }
            morphemes.append(tmp)
        node = node.next
    return morphemes


class Document:
    id: int
    body: str = ""
    morphemes: List[MorphemeCounter] = []
    wakati: List[str] = []
    length: int

    def __init__(self, body) -> None:
        self.morphemes = []
        self.body = body
        self.parseFromString(body)

    def getBody(self):
        return self.body

    def setId(self, id: int):
        self.id = id

    def parseFromString(self, body: str):
        result = parse(body)
        for one in result:
            self.wakati += one["surface"]
            self.add(Morpheme(one))

    def add(self, newMorpheme: Morpheme) -> None:
        flag = False
        for word in self.morphemes:
            if word.morpheme.surface == newMorpheme.surface and word.morpheme.wordClass == newMorpheme.wordClass:
                word.countUp()
                flag = True
        if not flag:
            self.morphemes.append(MorphemeCounter(newMorpheme))
            self.wakati.append(newMorpheme.surface)

    def sortByWordCount(self):
        return sorted(self.morphemes, key=lambda x: x.count, reverse=True)

    def filterByWordClasses(self, wordClasses: List[str]):
        self.morphemes = filter(
            lambda x: x.morpheme.wordClass in wordClasses, self.morphemes)
