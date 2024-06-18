from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/another')
def another_page():
    return 'This is another page!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
