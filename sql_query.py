# import sqlite3
# conn = sqlite3.connect('liu.db')
# cursor = conn.cursor()
# sql = '''
# SELECT * FROM people
# '''
# cursor.execute(sql)
# print(cursor.fetchall())

# cursor.close()
# conn.close()
# print('OK')


## # insert
import sqlite3
conn = sqlite3.connect('liu.db')
cursor = conn.cursor()

sql = '''
INSERT INTO  people(name, password) VALUES ('666', '777')
'''

cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
print('OK')

