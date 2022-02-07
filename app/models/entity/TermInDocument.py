from app.models.entity.Document import Document
import math


class Term:
    def __init__(self, args) -> None:
        self.surface = args["surface"]

        if "document_body" in args:
            id = args["document_id"] if "document_id" in args else False
            self.createDocument(args["document_body"], id)

        self.tf = args["tf"] if "tf" in args else 0
        self.df = args["df"] if "df" in args and args["df"] != 0 else 1

        self.calcIdf()
        self.calcTfIdf()

    def createDocument(self, body, id=False):
        self.document = Document(body).parseFromString()
        if id:
            self.document.setId(id)

    def calcTfIdf(self):
        self.tfIdf = self.tf * self.idf

    def calcIdf(self):
        self.idf = math.log(len(self.document.wakati)/self.df)
