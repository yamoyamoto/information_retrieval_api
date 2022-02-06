from typing import List


class Term:
    def __init__(self, args) -> None:
        self.surface = args["surface"]
        self.documentId = args["document_id"] if "document_id" in args else 0
        self.tf = args["tf"] if "tf" in args else 0
        self.idf = 1/args["df"] if "df" in args and args["df"] != 0 else 0
        self.calcTfIdf()

    def calcTfIdf(self):
        self.tfIdf = self.tf * self.idf
