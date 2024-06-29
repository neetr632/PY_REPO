import pymysql as mq
import random
import string 

def gen_rand_String(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digit, k=length))

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mysql.cursor()

try:
    for a in range(1):
        st_name = gen_rand_String(8)
        st_class = f"Grade{random.randint(1,13)}"
        st_email = f"{st_name.lower()}@example.com"
        
        insert_command = f"INSERT INTO student (st_name, st_class, st_email) VALUES ('{st_name}','{st_class}','{st_email}');"
        mycursor.execute(insert_command)
        
    mysql.commit()
    
    print("Rows inserted successfully!")

except Exception as e:
    mysql.rollback()
    print(f"Error: {e}")
    
finally:
    mycursor.close()
    mysql.close()