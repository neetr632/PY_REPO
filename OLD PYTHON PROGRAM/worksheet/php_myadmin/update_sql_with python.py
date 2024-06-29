import pymysql as mq
mysql=mq.connect( 
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=mysql.cursor()
try:
    UPDATE_command="UPDATE student SET st_email = 'ruby@gmail.co.in' WHERE st_id = 3"
   
    mycursor.execute(UPDATE_command)
    mysql.commit();
    print("Update successful")
except:
    print("Error...")