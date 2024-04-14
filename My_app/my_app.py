from flask import Flask

app = Flask(__name__)

@app.route('/GetNum/<int:a>/<int:b>')
def get_num(a, b):
    from random import randint
    return str(randint(a, b))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')