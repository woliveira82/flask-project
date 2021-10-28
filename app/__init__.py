from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/tests', methods=['GET'])
def get_tests():
    return 'ok'
