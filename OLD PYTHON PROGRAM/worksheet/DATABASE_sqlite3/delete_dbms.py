import sqlite3
conn = sqlite3.connect("testdbms.db")
st_id=input("Enter the st_id:-")
conn.execute("DELETE FROM student where st_id="+st_id)
conn.commit()
conn.close()