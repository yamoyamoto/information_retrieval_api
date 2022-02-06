import sqlite3
import os
from app.models.repository.DocumentRepository import DocumentRepository

docRepo = DocumentRepository()
documents = docRepo.getAll()

conn = sqlite3.connect(os.environ["DB_PATH"])
c = conn.cursor()

for document in documents:
    for morphemeCounter in document.morphemes:
        c.execute("INSERT INTO term_to_document (term, word_class, document_id, tf) VALUES (?, ?, ?, ?);",
                  (
                      morphemeCounter.morpheme.surface,
                      morphemeCounter.morpheme.wordClass,
                      document.id,
                      morphemeCounter.count,
                  )
                  )

conn.commit()
conn.close()
