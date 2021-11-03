from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
  	return render_template("./index.html")
    # return 'Hello, World!'

@app.route('/submit', methods=['POST'])
def yes():
  name= request.form['name']
  age= request.form['age']
  return '你好，' + name + ', 你的年龄是' + age
  
if __name__ == '__main__':
    app.run(host="0.0.0.0")
