import sqlite3
import os
import json

json_open = open("../document_data/corona.json", "r")
json_load = json.load(json_open)
data = json_load["data"]

bodies = []
for one in data:
    bodies.append(one["text"])

sql = "INSERT INTO document (body) VALUES "
sql += "(?), " * (len(data)-1) + "(?)"

conn = sqlite3.connect(os.environ["DB_PATH"])
c = conn.cursor()

c.execute(sql, bodies)

conn.commit()
conn.close()
