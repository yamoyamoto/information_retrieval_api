import sqlite3
import os

conn = sqlite3.connect(os.environ["DB_PATH"])

c = conn.cursor()

c.execute(
    "CREATE TABLE document (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT);"
)

# c.execute(
#     "CREATE TABLE term (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT, idf int);"
# )

c.execute(
    "CREATE TABLE term_to_document (id INTEGER PRIMARY KEY AUTOINCREMENT, term TEXT, word_class TEXT, document_id int, tf int, tf_idf int);"
)

conn.commit()
conn.close()
