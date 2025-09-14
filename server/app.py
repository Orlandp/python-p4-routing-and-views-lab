#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:text>")
def print_string(text):
    print(text)
    return text

@app.route("/count/<int:n>")
def count(n):
    lines = [str(i) for i in range(n)]
    return "\n".join(lines) + "\n"



@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return f"Invalid operation: {operation}", 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
