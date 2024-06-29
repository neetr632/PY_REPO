import pymysql as mq
conn=mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mysqlc=conn.cursor()
tc = "CREATE TABLE student (st_id INT AUTO_INCREMENT PRIMARY KEY, st_name VARCHAR(50), st_class VARCHAR(10), st_email VARCHAR(50))"
mysqlc.execute(tc)