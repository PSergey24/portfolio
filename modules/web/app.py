import os
import sys
sys.path.append(os.getcwd())
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/balance_parser')
def balance_parser():
    return render_template('balance_parser.html')


@app.route('/employees_parser')
def employees_parser():
    return render_template('employees_parser.html')
