import sqlite3

conn =sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()
data=[
    ('2020-02-01','buy','com',200,5.14),
    ('2020-02-02','buy','net',100,3.14),
    ('2020-02-03','buy','rhat',50,35.1),
    ('2020-02-04','buy','com',42,305.14)
    ]
sql='insert into stocks values(?,?,?,?,?)'
c.executemany(sql,data)
conn.commit()
conn.close()