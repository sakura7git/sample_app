import sqlite3

conn = sqlite3.connect("survey.db")

cursor = conn.execute("SELECT * FROM survey")

for row in cursor:
    print(row)

conn.close()