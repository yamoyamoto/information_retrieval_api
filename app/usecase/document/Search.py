from typing import List
from app.models.entity.Term import Term
from app.models.repository.TermRepository import TermRepository, toTermCorrection


class SearchDocumentAction:
    def __init__(self) -> None:
        pass

    def byTFIdf(self, query: str) -> List[Term]:
        repo = TermRepository()
        terms = repo.getBySurface(query)

        return sorted(terms, key=lambda x: x.tfIdf, reverse=True)

    def byCosine(self, query: str) -> List[Term]:
        repo = TermRepository()
        terms = repo.getBySurface(query)
        if len(terms) == 0:
            return []
        terms = toTermCorrection(terms).calcCosine()
        return sorted(terms, key=lambda x: x.cosine, reverse=True)
