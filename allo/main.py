from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Summary
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

# route sleep that takes a float number of seconds as a parameter
@app.route("/sleep/<float:seconds>")
def sleep(seconds):
    # sleep for the specified number of seconds
    time.sleep(seconds)
    return f"<p>Slept for {seconds} seconds</p>"

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8080)
