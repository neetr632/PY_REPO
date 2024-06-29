import pymysql as mq
# Specify your actual MySQL database credentials
# server name --> localhost
# username --> root
# password --> YOUR_ACTUAL_PASSWORD

# Creating a connection object
myobj = mq.connect(host="localhost", user="root", password="")
cursorobj = myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("db_created")

except:
    print("database error...")
# Close the connection
myobj.close()
