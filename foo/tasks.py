# coding: utf-8

from common import app

@app.task
def add(x, y):
    return x + y
