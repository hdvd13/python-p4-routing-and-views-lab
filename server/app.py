#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    return_val = ""
    for i in range(parameter):
        return_val += f"{i}\n"
    return return_val

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if(operation == "+"):
        return f"{int(num1)+int(num2)}"
    elif(operation == "-"):
        return f"{int(num1)-int(num2)}"
    elif(operation == "*"):
        return f"{int(num1)*int(num2)}"
    elif(operation == "div"):
        return f"{int(num1)/int(num2)}"
    elif(operation == "%"):
        return f"{int(num1)%int(num2)}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)