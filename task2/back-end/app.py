#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     # return render_template('index.html')
#     return "Hello World"

@app.route('/api/hello')
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # app.run(port=5250, host= "0.0.0.0")
    app.run(host='0.0.0.0', port=5252)
    