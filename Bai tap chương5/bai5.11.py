import sqlite3
conn = sqlite3.connect('ql_nhan_vien.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS PHONG(
                ID INTEGER PRIMARY KEY,
                Name TEXT Not Null,
                Price Real Not Null ,
                Amount INTEGER Not Null
                )
                '''
    )