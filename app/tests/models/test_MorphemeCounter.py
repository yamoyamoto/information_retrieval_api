import pytest

from app.models.entity.Morpheme import MorphemeCounter


class MorphemeStab:
    surface: str = "大阪"
    wordClass: str = "固有名詞"
    featureString: str = "名詞,固有名詞,地域,一般,*,*,大阪,オオサカ,オーサカ"


def testInitialize():
    morphemeStab = MorphemeStab()
    morphemeCounter = MorphemeCounter(morphemeStab)
    assert morphemeCounter.count == 1
    assert morphemeCounter.morpheme == morphemeStab


def testCountUp():
    morphemeStab = MorphemeStab()
    morphemeCounter = MorphemeCounter(morphemeStab)

    morphemeCounter.countUp()
    morphemeCounter.countUp()

    assert morphemeCounter.count == 3
