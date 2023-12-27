import sqlite3
conn = sqlite3.connect('mydatabase3.db')
cursor = conn.cursor()
cursor.execute("select count(ID)from USERS")
rows = cursor.fetchall()[0]
for row in rows:
    print(row)
conn.close()