import sqlite3
conn=sqlite3.connect("testdbms.db")
conn.execute(''' 
             UPDATE student SET st_name='ram1' WHERE st_id = 3
             ''')
conn.commit()
conn.close()