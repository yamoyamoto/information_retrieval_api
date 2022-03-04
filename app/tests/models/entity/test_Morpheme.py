from app.models.entity.Morpheme import Morpheme


def testInitialize():
    args = {
        "surface": "大阪",
        "feature": "名詞,固有名詞,地域,一般,*,*,大阪,オオサカ,オーサカ",
    }
    morpheme = Morpheme(args)

    assert morpheme.surface == "大阪"
    assert morpheme.featureString == "名詞,固有名詞,地域,一般,*,*,大阪,オオサカ,オーサカ"
    assert morpheme.wordClass == "名詞"
