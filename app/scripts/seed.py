import sqlite3
import os
import math
from app.models.repository.DocumentRepository import DocumentRepository

docRepo = DocumentRepository()
documents = docRepo.getAll()
documentNum = len(documents)

conn = sqlite3.connect(os.environ["DB_PATH"])
c = conn.cursor()

for document in documents:
    document.parseFromString()
    for morphemeCounter in document.morphemes:
        c.execute("INSERT INTO term_to_document (term, word_class, document_id, tf) VALUES (?, ?, ?, ?);",
                  (
                      morphemeCounter.morpheme.surface,
                      morphemeCounter.morpheme.wordClass,
                      document.id,
                      morphemeCounter.count / len(document.morphemes),
                  )
                  )

c.execute("""UPDATE term_to_document
    SET df=b.df
    FROM (
        SELECT term, COUNT(*) as df FROM term_to_document GROUP BY term
    ) as b
    WHERE term_to_document.term=b.term;
    """)

c.execute("SELECT id, tf, df FROM term_to_document;")
allTerms = c.fetchall()
for term in allTerms:
    c.execute("UPDATE term_to_document SET tf_idf=? WHERE id=?;",
              (term[1] * math.log(documentNum / term[2]), term[0]))

conn.commit()
conn.close()
