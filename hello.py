from flask import Flask, escape, request, abort
from prometheus_client import make_wsgi_app, Counter, Gauge, Histogram
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

INFO = Gauge('build_info', 'Information about the application', ['version'])
INFO.labels('1.0.0').set(1)
HELLO_COUNTER = Counter('hellos', 'Total number of hellos')
HELLO_FAILED_COUNTER = Counter('hellos_failed', 'Total number of failed hellos')
LATENCY = Histogram('hellos_latency_seconds', 'Histogram of latency')

@app.route('/')
@LATENCY.time()
def hello():
    HELLO_COUNTER.inc()
    try:
        name = request.args["name"]
        return f'Hello, {escape(name)}!'
    except:
        HELLO_FAILED_COUNTER.inc()
        abort(500)

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
