import sqlite3
#Viết chương trình Python để cập nhất tất cả các giá trị của một cột cụ thể trong bảng SQLite 'mydatevasse.db'  
conn = sqlite3.connect('mydatabase3.db')
cursor = conn.cursor()
cursor.execute("UPDATE USERS SET Tuổi = 40")
conn.commit()
cursor.execute("SELECT * FROM USERS")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()