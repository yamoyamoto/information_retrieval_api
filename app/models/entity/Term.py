from app.models.entity.Document import Document
from typing import List

INF = 100000


class Term:
    def __init__(self, args) -> None:
        # print(args)
        self.id = args["id"]
        self.surface = args["surface"]
        self.createDocument(args["document_body"], args["document_id"])
        self.tf = args["tf"]
        self.df = args["df"]
        self.tfIdf = args["tf_idf"]
        self.document_count = args["document_count"]

    def createDocument(self, body, id=False):
        self.document = Document(body).parseFromString()
        self.N = len(self.document.wakati)
        if id:
            self.document.setId(id)

    def setInnerProduct(self, innerProduct: int):
        self.innerProduct = innerProduct
        return self

    def setCosine(self, cosine):
        self.cosine = cosine
        return self


class TermCorrection:
    terms: List[Term]

    def __init__(self, terms) -> None:
        self.terms = terms
        pass

    def calcNorm(self):
        norm = 0
        for term in self.terms:
            norm += term.idf ** 2
        if norm <= 0:
            raise Exception("norm must be more than 0")
        return norm

    def calcCosine(self) -> List[Term]:
        returnTerms = []
        for term in self.terms:
            # queryを分解しないのでtf-idfが内積になる
            returnTerms.append(term.setInnerProduct(term.tfIdf))
        return self
