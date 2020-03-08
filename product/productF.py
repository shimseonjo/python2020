import pymysql

def conndb():
    conn = pymysql.connect(host='maria',
                        user='root',
                        password='qwer1234',
                        db='test',
                        cursorclass=pymysql.cursors.DictCursor)
    return conn

def createTable():
    conn=conndb()
    c = conn.cursor()
    sql='drop table product'
    c.execute(sql)
    sql='''
        create table if not exists product(
            product_id int,
            product_name varchar(50),
            price int default 0,
            description text,
            picture_url varchar(500),
            CONSTRAINT PRIMARY KEY (product_id)
        )
    '''
    c.execute(sql)
    conn.commit()
    conn.close()

def insertdata():
    conn=conndb()

def listdata():
    conn=conndb()

def serchdata():
    conn=conndb()

def updatedata():
    conn=conndb()

def deletedata():
    conn=conndb()
