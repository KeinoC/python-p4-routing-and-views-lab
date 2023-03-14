#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'

@app.route("/count/<parameter>")
def count(parameter):
    for x in range(0, parameter):
        print (f'{x} \n')

@app.route("/math/<num1><operation><num2>")
def math(num1, operation,num2):
    if (operation == "+"):
        print (num1 / num2)
    elif (operation == "-"):
        print(num1 - num2)
    elif (operation == "*"):
        print(num1 * num2)
    elif (operation == "div"):
        print(num1 / num2)
    elif (operation == "%"):
        print(num1 % num2)

    
    


