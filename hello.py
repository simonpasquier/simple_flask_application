from flask import Flask, escape, request, abort
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        name = request.args["name"]
        return f'Hello, {escape(name)}!'
    except:
        abort(500)

app_dispatch = DispatcherMiddleware(app)
