# coding : utf-8
import sys
import flask
import threading

app=flask.Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    args = sys.argv
    return 'port is {}'.format(args[1])

@app.route('/index', methods=['post', 'get'])
def ll():
    args = sys.argv
    return 'index port is {}'.format(args[1])

port = sys.argv[1]


app.run(port=int(port))

