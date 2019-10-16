A very simple project demonstrating how to instrument a [Flask](https://palletsprojects.com/p/flask/) application with [Prometheus](https://prometheus.io).

To run the application:

```bash
virtualenv .
pip install -r requirements.txt
./run.sh
```

The application runs on `localhost:8000` and greets the client expect if the `name` request parameter is `crash`.

```bash
$ curl localhost:8000/
Hello, World!
$ curl localhost:8000/?name=Simon
Hello, Simon!
$ curl localhost:8000/?name=crash
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
```

There are 2 active branches:

* [master](https://github.com/simonpasquier/simple_flask_application/tree/master) with only the HTTP endpoint.
* [instrumented](https://github.com/simonpasquier/simple_flask_application/tree/instrumented) with Prometheus metrics available at `/metrics`. In addition to the Python and process metrics, the application exposes `hellos_created`, `hellos_total`, `hellos_failed_created`, and `hellos_failed_total`.
