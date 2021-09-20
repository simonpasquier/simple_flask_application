from flask import Flask, escape, request, abort
from prometheus_client import make_wsgi_app, Counter, Gauge, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

INFO = Gauge('build_info', 'Information about the application', ['version'])
INFO.labels('1.0.0').set(1)

HTTP_COUNTER = Counter('http_requests', 'Total number of HTTP requests per status code', ['code'])

LATENCY = Histogram('hellos_latency_seconds', 'Histogram of latency for hello requests',
        buckets=(.0001, .0002, .0003, .0004, .0005))

@app.route('/')
def hello():
    with LATENCY.time():
        try:
            name = request.args["name"]
            return f'Hello, {escape(name)}!'
        except:
            abort(500)

@app.after_request
def after_request_func(response):
    HTTP_COUNTER.labels(code=response.status_code).inc()
    return response

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
