from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/add', methods=['POST'])
def add():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return str(result)

#@app.route('/subtract', methods=['POST'])
def subtract():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 - num2
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
