from cgitb import reset

# "-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"

# Counterの排除 → WrapperにCount情報をもたせる
# 永続化方法の検討(Documentと突き合わせて保存する必要がある)


class Morpheme:
    featureString: str
    surface: str
    wordClass: str

    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.featureString = args["feature"]
        self.parseFeatureString()

    def parseFeatureString(self):
        arr = self.featureString.split(",")
        self.wordClass = arr[0]


class MorphemeCounter:
    morpheme: Morpheme
    count: int

    def __init__(self, morpheme: Morpheme) -> None:
        self.morpheme = morpheme
        self.count = 1

    def countUp(self):
        self.count += 1
