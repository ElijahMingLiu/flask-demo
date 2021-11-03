from flask import Flask, render_template, request
import sqlite3

def get_user(name):
    conn = sqlite3.connect('liu.db')
    cursor = conn.cursor()
    sql = '''
    SELECT * FROM people WHERE name='{}'
    '''.format(name)
    cursor.execute(sql)
    
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def get_user_pass(name, password):
    conn = sqlite3.connect('liu.db')
    cursor = conn.cursor()
    sql = '''
    SELECT * FROM people WHERE name='{}' AND password='{}'
    '''.format(name, password)
    cursor.execute(sql)
    
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def new_user(name, password):
    conn = sqlite3.connect('liu.db')
    cursor = conn.cursor()

    sql = '''
    INSERT INTO  people(name, password) VALUES ('{}', '{}')
    '''.format(name, password)

    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    password = request.form['password']

    if len(get_user(name)) > 0:


        return '用户名重复！'
    else :
        new_user(name, password)
        return '注册成功！'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['password']

    if len(get_user(name)) > 0 and get_user_pass(name, password):

        return '登录成功！'
    elif len(get_user(name)) > 0:
        return '密码错误！'
    else:
        return '用户不存在'

if __name__ == '__main__':
    try:
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
    except:
        pass

    app.run(host="0.0.0.0")