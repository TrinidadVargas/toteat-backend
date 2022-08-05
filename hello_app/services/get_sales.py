import os
import json

def get_sales():
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, '../static/sales.json')
  print(dirname, filename)
  with open(filename) as file:
    data = json.load(file)
  return data