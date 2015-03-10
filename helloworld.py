from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Hello world, from flask. At last! ;)'


if __name__ == '__main__':
    app.run()