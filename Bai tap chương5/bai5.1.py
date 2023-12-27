import sqlite3
conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()
cursor.execute('select sqlite_version()')
print(cursor.fetchall())
conn.close()