from flask import Flask, escape, request, abort
from werkzeug.middleware.dispatcher import DispatcherMiddleware

import prometheus_client

INFO = prometheus_client.Gauge('hello_app_info', 'Hello applicatoin information', ['version'])
INFO.labels('1.0.0').set(1)

HTTP_COUNTER = prometheus_client.Counter('hello_app_http_requests', 'Total number of HTTP requests per status code', ['code'])
LATENCY = prometheus_client.Histogram('hello_app_latency_seconds', 'Histogram of latency for hello requests',
        buckets=(.0001, .0002, .0003, .0004, .0005))

app = Flask(__name__)

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
    '/metrics': prometheus_client.make_wsgi_app()
})
