import sqlite3
conn = sqlite3.connect("testdbms.db")

insert = '''
insert into student (st_name,st_class,st_email) VALUES ('RAVIRR ','12th','ram@gmail.com')

'''
conn.execute(insert)
conn.commit()
conn.close()
