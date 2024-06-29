import pymysql as mq
mysql=mq.connect( 
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=mysql.cursor()
try:
    insert_command="INSERT INTO student (st_name,st_class,st_email) values(%s,%s,%s)"
    data_tobe_inserted=("ruby",'1th','ruby@gmail.com')
    mycursor.execute(insert_command,data_tobe_inserted)
    mysql.commit();
    print("Insert Data")
except:
    print("Error...")