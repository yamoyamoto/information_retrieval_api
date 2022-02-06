from app.models.entity.Document import Document
import math


class TermInDocument:
    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.documentId = args["document_id"] if "document_id" in args else 0
        self.document = Document(
            args["document_body"]).parseFromString() if "document_body" in args else ""

        self.tf = args["tf"] if "tf" in args else 0
        self.df = args["df"] if "df" in args and args["df"] != 0 else 1

        self.calcIdf()
        self.calcTfIdf()

    def calcTfIdf(self):
        self.tfIdf = self.tf * self.idf

    def calcIdf(self):
        self.idf = math.log(len(self.document.wakati)/self.df)
