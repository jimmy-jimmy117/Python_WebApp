from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def inex():
    return "Response Data"


@app.route("/another")
def inex2():
    return "Another Response"


@app.route("/test_request")
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route("/exercise_request/<dummy>")
def test_request2(dummy):
    return f"exercise_request;{dummy}"
