import sqlite3
conn = sqlite3.connect('mydatabase2.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM USERS")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()