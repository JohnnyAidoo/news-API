from flask import Flask, jsonify
from fetch import data


app = Flask(__name__)


@app.route('/')
def index():
    return('Nothing Here')

@app.route('/api')
def api():
    return jsonify(data)


if __name__ == '__main__':
    app.run()