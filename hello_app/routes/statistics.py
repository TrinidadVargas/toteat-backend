from datetime import datetime
from flask import Flask, request, jsonify
from .. import app
from ..use_cases import sales_by_period, sales_summary

@app.route('/statistics/')
def index():
    return 'Hello World!'

@app.route('/statistics/sales_by_period/')
def sales_by_period_route():
    data = sales_by_period(request.args)
    response = jsonify({'data': data})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/statistics/sales_summary/')
def sales_summary_route():
    data = sales_summary(request.args, None)
    response = jsonify({'data': data})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
