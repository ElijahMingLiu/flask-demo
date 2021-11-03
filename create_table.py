import sqlite3
conn = sqlite3.connect('liu.db')
cursor = conn.cursor()
sql = '''
CREATE TABLE 
people(
    name varchar(20) primary key,
    password varchar(20)
)
'''
cursor.execute(sql)

cursor.close()
conn.close()
print('OK')

