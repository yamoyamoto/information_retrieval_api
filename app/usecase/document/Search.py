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
