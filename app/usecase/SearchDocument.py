from typing import List
from app.models.entity.TermInDocument import TermInDocument
from app.models.repository.TermRepository import TermRepository


class SearchDocumentUseCase:
    def __init__(self) -> None:
        pass

    def byTFIdf(self, query: str) -> List[TermInDocument]:
        repo = TermRepository()
        terms = repo.getBySurface(query)

        return sorted(terms, key=lambda x: x.tfIdf)
