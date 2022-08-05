from datetime import datetime
from flask import Flask, request, jsonify
from .. import app
# from ..use_cases import sales_by_day
from ..use_cases import sales_by_period

@app.route('/statistics/')
def index():
    return 'Hello World!'

@app.route('/statistics/sales_by_period/')
def sales_by_period_route():
    data = sales_by_period(request.args)
    response = jsonify({'data': data})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
