from datetime import datetime
from flask import Flask, request, jsonify
from .. import app
# from ..use_cases import sales_by_day
from ..use_cases import sales_by_day

@app.route('/statistics/')
def index():
    return 'Hello World!'


@app.route('/statistics/income_by_day/')
def sales_by_day_route():
    data = sales_by_day(request.args)
    return jsonify({'data': data})