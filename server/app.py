#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views.</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<p>Printed string : {param}</p>'

@app.route('/count/<int:param>')
def count(param):
    numbers = range(1, param + 1)
    numbers_html = "<ul>"
    for number in numbers :
        numbers_html += f"<li>{number}</li>"
    numbers_html += "</ul>"
    return numbers_html

@app.route('/math/<float:num1><operation><float:num2>')
def math (num1, operation , num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 -num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero cannot work"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."
    return f'Result of {num1} {operation} {num2} is {result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
