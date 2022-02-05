import sqlite3
import os

conn = sqlite3.connect(os.environ["DB_PATH"])

c = conn.cursor()

c.execute(
    "CREATE TABLE document (id int, body TEXT)"
)

c.execute(
    "INSERT INTO document (id, body) VALUES (1, '川口友也は大阪生まれ、大阪出身です。');"
)

conn.commit()
conn.close()
