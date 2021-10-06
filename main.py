import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello_world():
    return '''<h1>Hello World</h1>'''

app.run()