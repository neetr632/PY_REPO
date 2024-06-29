import pymysql as mq
import random
import string

def generate_random_string(length=8):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

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
    # Insert 6 rows with random details
    for _ in range(1):
        st_name = generate_random_string(8)
        st_class = f"Grade {random.randint(1, 12)}"
        st_email = f"{st_name.lower()}@example.com"

        insert_command = f"INSERT INTO student (st_name, st_class, st_email) VALUES ('{st_name}', '{st_class}', '{st_email}');"
        mycursor.execute(insert_command)

    # Commit the changes to the database
    mysql.commit()

    print("Rows inserted successfully!")

except Exception as e:
    # If an error occurs, rollback the changes
    mysql.rollback()
    print(f"Error: {e}")

finally:
    # Close the cursor and the connection
    mycursor.close()
    mysql.close()
