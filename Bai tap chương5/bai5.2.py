import sqlite3
#viết chương trình để tạo kết nối đến cơ sở dữ liueej sqlite tới cơ sở dữ liệu nằm trong bộ nhớ
conn = sqlite3.connect(':memory:')
#tạo một đối tượng con trỏ từ đối tượng kết nối
conn.close()