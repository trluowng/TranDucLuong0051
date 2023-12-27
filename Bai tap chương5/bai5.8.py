import sqlite3
conn = sqlite3.connect('mydatabase3.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM USERS WHERE ID = 1")
conn.commit()
cursor.execute("select * from USERS")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
