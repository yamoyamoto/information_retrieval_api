from array import array
# "-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"


class MecabWord:
    featureString: str
    surface: str
    wordClass: str

    def __init__(self, surface) -> None:
        self.surface = surface

    def parseFeatureString(self, payload: str):
        # self.featureString = payload
        arr = payload.split(",")
        self.wordClass = arr[1]


class MecabWordWithCounter:
    mecabWord: MecabWord
    count: int

    def __init__(self, mecabWord: MecabWord) -> None:
        self.mecabWord = mecabWord
        self.count = 1

    def countUp(self):
        self.count += 1


class MecabSentence:
    mecabWords: array = []
    wakati: str = ""

    def __init__(self) -> None:
        self.mecabWords = []

    def add(self, newMecabWord: MecabWord) -> None:
        flag = False
        for word in self.mecabWords:
            if word.mecabWord.surface == newMecabWord.surface and word.mecabWord.wordClass == newMecabWord.wordClass:
                word.countUp()
                flag = True
        if not flag:
            self.mecabWords.append(MecabWordWithCounter(newMecabWord))
            self.wakati += newMecabWord.surface

    def sort(self):
        return sorted(self.mecabWords, key=lambda x: x.count, reverse=True)

    def filter(self, wordClasses: array):
        self.mecabWords = filter(
            lambda x: x.mecabWord.wordClass in wordClasses, self.mecabWords)
        return self.mecabWords
