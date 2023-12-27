import sqlite3
conn = sqlite3.connect('mydatabase3.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                "Tên" TEXT,
                "Tuổi" INTEGER 
                )
                '''
    )
cursor.execute('''INSERT INTO USERS 
                VALUES (2, "Nguyễn Văn B", 20)''')
conn.commit()

cursor.execute("SELECT * FROM USERS")   
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()