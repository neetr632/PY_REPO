import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("testdbms.db")

# Execute the SELECT query
data = conn.execute("SELECT * FROM student WHERE st_id limit 10,13")

# Fetch and print the results
for n in data:
    print(n[0], "", n[1], "", n[2], n[3])

# Close the connection
conn.close()
