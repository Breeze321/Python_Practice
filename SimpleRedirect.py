#!/usr/bin/env python3

from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://example.com')

if __name__ == '__main__':
    app.run(debug=True)
