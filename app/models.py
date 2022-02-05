from array import array
# "-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"


class Morpheme:
    featureString: str
    surface: str
    wordClass: str

    def __init__(self, surface) -> None:
        self.surface = surface

    def parseFeatureString(self, payload: str):
        self.featureString = payload
        arr = payload.split(",")
        self.wordClass = arr[1]


class MorphemeWithCounter:
    morpheme: Morpheme
    count: int

    def __init__(self, morpheme: Morpheme) -> None:
        self.morpheme = morpheme
        self.count = 1

    def countUp(self):
        self.count += 1


class MecabSentence:
    morphemes: array = []
    wakati: str = ""

    def __init__(self) -> None:
        self.morphemes = []

    def add(self, newMorpheme: Morpheme) -> None:
        flag = False
        for word in self.morphemes:
            if word.morpheme.surface == newMorpheme.surface and word.morpheme.wordClass == newMorpheme.wordClass:
                word.countUp()
                flag = True
        if not flag:
            self.morphemes.append(MorphemeWithCounter(newMorpheme))
            self.wakati += newMorpheme.surface

    def sortByWordCount(self):
        return sorted(self.morphemes, key=lambda x: x.count, reverse=True)

    def filter(self, wordClasses: array):
        return filter(
            lambda x: x.morpheme.wordClass in wordClasses, self.morphemes)
