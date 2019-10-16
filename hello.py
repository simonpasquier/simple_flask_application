from flask import Flask, escape, request, abort
from prometheus_client import make_wsgi_app, Counter
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

HELLO_COUNTER = Counter('hellos', 'Total number of hellos')
HELLO_FAILED_COUNTER = Counter('hellos_failed', 'Total number of hellos')

@app.route('/')
def hello():
    HELLO_COUNTER.inc()
    name = request.args.get("name", "World")
    if name == "crash":
        HELLO_FAILED_COUNTER.inc()
        abort(500)
    return f'Hello, {escape(name)}!'

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
