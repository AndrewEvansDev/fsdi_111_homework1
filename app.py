#!/usr/bin/env python3
"""Basic Hello world app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/aboutme")
def about():
    me = {
        'first_name':'andrew',
        'last_name':'evans',
        'hobbies':'wine drinking',
        'ok':True
    }
    return render_template("about.html", user=me)