from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded username and password
USERNAME = "sbe3"
PASSWORD = "123"

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return "Login successful!"
    else:
        return "Login failed. Incorrect username or password."

if __name__ == '__main__':
    app.run(debug=True)
