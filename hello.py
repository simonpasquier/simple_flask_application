from flask import Flask, escape, request, abort
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    if name == "crash":
        abort(500)
    return f'Hello, {escape(name)}!'

app_dispatch = DispatcherMiddleware(app)
