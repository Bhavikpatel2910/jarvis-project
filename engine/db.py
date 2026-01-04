import sqlite3
import csv

con= sqlite3.connect('jarvis.db')
cursor = con.cursor()

# query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), Url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'gtu student portal ', 'hhttps://student.gtu.ac.in/')"
# cursor.execute(query)
# con.commit()


