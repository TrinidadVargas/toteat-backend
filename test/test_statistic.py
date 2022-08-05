from hello_app.use_cases import sales_by_specific_period

sale_data = {
    "date_closed": "2019-03-18 15:40:47", 
    "zone": "Salón",
    "waiter": "María José Perez", 
    "cashier": "Roberto Ortega", 
    "products": [
        { "category": "Bebidas", "price": 2000, "name": "Café", "quantity": 1}, 
        {"category": "Tragos", "price": 2500, "name": "Cerveza", "quantity": 1}
    ], 
    "diners": 2,
    "date_opened": "2019-03-18 14:04:01",
    "table": 7,
    "total": 4500,
    "id": "1ea97de85eb634d580161c603422437f",
    "payments": [{"amount": 4500, "type": "Efectivo"}]
}

def test_sale_by_day():
    args = []
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['total'] == 4500

def test_sale_by_day_waiter():
    args = ['waiter']
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['waiter']['María José Perez'] == 4500

def test_sale_by_day_cashier():
    args = ['cashier']
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['cashier']['Roberto Ortega'] == 4500

def test_sale_by_day_zone():
    args = ['zone']
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['zone']['Salón'] == 4500

def test_sale_by_day_lunch():
    args = ['time']
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['time']['lunch'] == 4500

def test_sale_by_day_dinner():
    args = ['time']
    result = sales_by_specific_period([sale_data], args, period='day')
    assert result[0]['time']['dinner'] == 0
