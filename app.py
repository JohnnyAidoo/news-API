from flask import Flask, jsonify
from fetch import data
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return('Nothing Here')

@app.route('/api')
def api():
    load = json.loads(data)
    return (load)


if __name__ == '__main__':
    app.run()