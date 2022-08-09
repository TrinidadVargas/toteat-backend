from hello_app.use_cases import sales_by_specific_period

sale_data = [{
        "date_closed": "2019-03-18 15:40:47", 
        "zone": "Salón",
        "waiter": "María José Perez", 
        "cashier": "Roberto Ortega", 
        "products": [],
        "diners": 2,
        "date_opened": "2019-03-18 14:04:01",
        "table": 7,
        "total": 4500,
        "id": "1ea97de85eb634d580161c603422437f",
        "payments": [{"amount": 4500, "type": "Efectivo"}]
    },
    {
        "date_closed": "2019-03-18 15:31:42",
        "zone": "Salón",
        "waiter": "Cristian Eiler",
        "cashier": "Sebastian Hernandez",
        "products": [],
        "diners": 6,
        "date_opened": "2019-03-18 15:12:52",
        "table": 10,
        "total": 138750,
        "id": "73f104c9fba50050eea11d9d075247cc",
        "payments": [{"amount": 138750, "type": "Tarjeta crédito"}]
    }
]

def test_sale_by_day_total():
    args = []
    result = sales_by_specific_period(sale_data, args, period='day')
    assert result[0]['all']['total'] == 143250

def test_sale_by_day_min():
    args = []
    result = sales_by_specific_period(sale_data, args, period='day')
    assert result[0]['all']['min'] == 4500

def test_sale_by_day_max():
    args = []
    result = sales_by_specific_period(sale_data, args, period='day')
    assert result[0]['all']['max'] == 138750

def test_sale_by_day_num_sales():
    args = []
    result = sales_by_specific_period(sale_data, args, period='day')
    assert result[0]['all']['num_sales'] == 2
