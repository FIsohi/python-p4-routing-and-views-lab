from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print the string to the console
    return f'<p>{text}</p>'  # Display the string in the web browser

@app.route('/count/<int:number>')
def count(number):
    return '<br>'.join(str(i) for i in range(number + 1))  # Display numbers from 0 to `number`

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Bad Request if operation is invalid
    return f'<p>Result of {num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
