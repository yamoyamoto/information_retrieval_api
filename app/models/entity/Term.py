from app.models.entity.Document import Document
import math

INF = 100000


class Term:
    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.createDocument(args["document_body"], args["document_id"])
        self.tf = args["tf"]
        self.df = args["df"]

        self.calcIdf()
        self.calcTfIdf()

    def createDocument(self, body, id=False):
        self.document = Document(body).parseFromString()
        if id:
            self.document.setId(id)

    def calcTfIdf(self):
        self.tfIdf = self.tf * self.idf

    def calcIdf(self):
        if self.df == 0:
            self.idf = INF
        else:
            self.idf = math.log(len(self.document.wakati)/self.df)
