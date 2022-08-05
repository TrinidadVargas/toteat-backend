import json

def get_sales():
  file_name = './static/sales.json'
  with open(file_name) as file:
    data = json.load(file)
  return data