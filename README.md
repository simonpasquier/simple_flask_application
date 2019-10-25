A very simple project demonstrating how to instrument a [Flask](https://palletsprojects.com/p/flask/) application with [Prometheus](https://prometheus.io).

## Running the application

The usual way to install and run the app is to setup a virtual environment.

```bash
virtualenv .
pip install -r requirements.txt
./run.sh
```

The application runs on `localhost:3000`, it expects a `name` request and sends a greet message. It will return a `500` code if the parameter is missing.

```bash
$ curl localhost:3000/?name=Simon
Hello, Simon!
$ curl localhost:3000/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
```

There are 2 active branches:

* [master](https://github.com/simonpasquier/simple_flask_application/tree/master) with only the HTTP endpoint.
* [instrumented](https://github.com/simonpasquier/simple_flask_application/tree/instrumented) with Prometheus metrics available at `/metrics` ([master diff](https://github.com/simonpasquier/simple_flask_application/compare/instrumented)). In addition to the Python and process metrics, the application exposes `hellos_created`, `hellos_total`, `hellos_failed_created`, and `hellos_failed_total`.

## Running the demo

First make sure that the following binaries are in your PATH:

* [`prometheus`](https://github.com/prometheus/prometheus/)
* [`alertmanager`](https://github.com/prometheus/alertmanager/)
* [`loadtest`](https://github.com/simonpasquier/loadtest)
* [`goreman`](https://github.com/mattn/goreman)

Then run `goreman start`.

The Prometheus UI is available at `http://localhost:9090/` and Alertmanager at `http://localhost:9093/`.

## License

Apache License 2.0, see [LICENSE](https://github.com/simonpasquier/simple_flask_application/blob/master/LICENSE).
