import sqlite3
conn = sqlite3.connect('mydatabase2.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
               ID INTEGER PRIMARY KEY,
               "Tên" TEXT,
               "Tuổi" INTEGER 
               )
               '''
)
conn.close()