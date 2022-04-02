from decimal import Decimal
import math
from typing import List
from app.models.entity.Term import Term
from app.models.repository.TermRepository import TermRepository


class SearchDocumentAction:
    def __init__(self) -> None:
        pass

    def byTFIdf(self, query: str) -> List[Term]:
        repo = TermRepository()
        terms = repo.getBySurface(query)

        return sorted(terms, key=lambda x: x.tfIdf, reverse=True)

    def byCosine(self, query: str):
        repo = TermRepository()
        terms = repo.getBySurface(query)
        if len(terms) == 0:
            return []

        termsWithCosine: List[Term] = []

        for term in terms:
            norm = repo.fetchNormById(term.document.id)
            cosine = term.tfIdf / math.sqrt(norm)
            termsWithCosine.append(term.setCosine(cosine))

        termsWithCosine = sorted(
            termsWithCosine, key=lambda x: x.cosine, reverse=True)

        return termsWithCosine
