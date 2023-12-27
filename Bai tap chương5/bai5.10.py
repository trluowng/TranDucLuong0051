import sqlite3
conn = sqlite3.connect('product.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS product(
                ID INTEGER PRIMARY KEY,
                Name TEXT Not Null,
                Price Real Not Null ,
                Amount INTEGER Not Null
                )
                '''
    )
conn.commit()
def hien_thi ():
    cursor.execute('''select * from product''')
    row = cursor.fetchall()
    for i in row:
        print(i)
def them(id,name,price):
    cursor.execute('''Insert into product(ID,Name,Price) values(?,?,?)''',(id,name,price))
    conn.commit()
def update(id,price,amount):
    cursor.execute('''update product set Price = {} where ID = {}'''.format(price,id))
    conn.commit()
    cursor.execute('''update product set Amount = {} where ID = {}'''.format(amount,id))
    conn.commit()
def delete(id):
    cursor.execute('''delete from product where ID = {}'''.format(id))
    conn.commit()
def search(name):
    cursor.execute('''select * from product where name = {}'''.format(name))
