import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("testdbms.db")

# Create the "student" table
conn.execute('''
    CREATE TABLE student (
        st_id INTEGER PRIMARY KEY AUTOINCREMENT,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
