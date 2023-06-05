from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Allô, tout le monde!</p>"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
