from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    input_data = request.json

    if "first" not in input_data or "second" not in input_data:
        return 'Missing required parameters', 400

    first = input_data["first"]
    second = input_data["second"]
    result = first + second

    response = {
        "result": result
    }

    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    input_data = request.json

    if "first" not in input_data or "second" not in input_data:
        return 'Missing required parameters', 400

    first = input_data["first"]
    second = input_data["second"]
    result = first - second

    response = {
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
