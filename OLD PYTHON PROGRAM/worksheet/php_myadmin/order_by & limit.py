import pymysql as mq

# Establish a connection to the MySQL server
mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Create a cursor object to interact with the database
mycursor = mysql.cursor()

try:
    # SQL command to select data ordered by st_id and limit the result to 5 rows
    select_command = "SELECT * FROM student ORDER BY st_id LIMIT 50;"

    # Execute the SQL command
    mycursor.execute(select_command)

    # Fetch all the rows from the result set
    result = mycursor.fetchall()

    # Print the result
    for row in result:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and the connection
    mycursor.close()
    mysql.close()
