from app.models.entity.Document import Document
import math
from decimal import Decimal, ROUND_HALF_UP
from typing import List

INF = 100000


class Term:
    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.createDocument(args["document_body"], args["document_id"])
        self.tf = args["tf"]
        self.df = args["df"]
        self.document_count = args["document_count"]

        self.__calcTf()
        self.__calcIdf()
        self.__calcTfIdf()

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

    def __calcTf(self):
        self.tf = Decimal(self.tf / self.N)

    def __calcTfIdf(self):
        self.tfIdf = self.tf * self.idf

    def __calcIdf(self):
        if self.df == 0:
            self.idf = INF
        else:
            self.idf = math.log(self.document_count/self.df)
            self.idf = Decimal(str(self.idf)).quantize(
                Decimal("0.001"), rounding=ROUND_HALF_UP)


class TermCorrection:
    terms: List[Term]

    def __init__(self, terms) -> None:
        self.terms = terms
        pass

    def calcCosine(self) -> List[Term]:
        norm = 0
        returnTerms = []
        for term in self.terms:
            norm += term.idf
            # queryを分解しないのでtfが内積になる
            returnTerms.append(term.setInnerProduct(term.tf))
        if norm <= 0:
            raise Exception("norm must be more than 0")
        return self.__setCosineToTerms(norm)

    def __setCosineToTerms(self, norm):
        returnTerms = []
        for term in self.terms:
            cosine = term.innerProduct / Decimal(math.sqrt(norm))
            returnTerms.append(term.setCosine(cosine))
        return returnTerms
