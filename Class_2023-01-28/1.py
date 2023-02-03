import sqlite3






conn = sqlite3.connect('E:\git\py\pexelpro_bot\data.db')


conn.execute("INSERT INTO RECORDS (id, user, subject, message, attachment, status)             VALUES (0,'Artur','1','2','','')")
conn.commit()
conn.close()