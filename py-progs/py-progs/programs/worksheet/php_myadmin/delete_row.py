import pymysql as mq
mysql=mq.connect( 
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=mysql.cursor()
DELETE_command="DELETE FROM student WHERE st_id = 3"
try:  
    mycursor.execute(DELETE_command)
    mysql.commit();
    print("DELETE STUDENT DETAILS SUCCESSFULLY")
except:
    print("Error...")