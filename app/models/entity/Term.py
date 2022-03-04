from app.models.entity.Document import Document
import math
from decimal import Decimal, ROUND_HALF_UP

INF = 100000


class Term:
    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.createDocument(args["document_body"], args["document_id"])
        self.tf = args["tf"]
        self.df = args["df"]

        self.__calcTf()
        self.__calcIdf()
        self.__calcTfIdf()

    def createDocument(self, body, id=False):
        self.document = Document(body).parseFromString()
        self.N = len(self.document.wakati)
        if id:
            self.document.setId(id)

    def __calcTf(self):
        self.tf = Decimal(self.tf / self.N)

    def __calcTfIdf(self):
        self.tfIdf = self.tf * self.idf

    def __calcIdf(self):
        if self.df == 0:
            self.idf = INF
        else:
            self.idf = math.log(self.N/self.df)
            self.idf = Decimal(str(self.idf)).quantize(
                Decimal("0.001"), rounding=ROUND_HALF_UP)
