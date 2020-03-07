import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()

c.execute('select * from stocks')
print(c.fetchall())
symbol=input('심볼을 입력하세요')
sql="select * from stocks where symbol='%s'"%symbol
sql="select * from stocks where symbol=?"
c.execute(sql,[symbol])
print(c.fetchall())
conn.close()