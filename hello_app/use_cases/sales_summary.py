from collections import defaultdict
from datetime import datetime
from ..services import get_sales

filters_allowed = ['date_start', 'date_end', 'hour_start', 'hour_end']
details_allowed = ['waiter', 'cashier', 'zone', 'table']

def sales_summary(filters, details):
    sales = get_sales()
    if filters:
        sales = [sale for sale in sales if filter_sale(sale, filters)]
    details = ['waiter', 'cashier', 'zone', 'table']
    data = summary_dict_init(details)
    for sale in sales:
        add_data(data['all'], sale)
        for detail in details:
            data[detail][sale[detail]]['name'] = sale[detail]
            add_data(data[detail][sale[detail]], sale)
    data['details'] = data_details(sales, filters, details)
    return data

def filter_sale(sale, filters):
    sale_date = to_date(sale['date_opened'].split()[0])
    for key, value in filters.items():
        if key in ['waiter', 'cashier', 'zone', 'table'] and sale[key] not in value:
            return False
        elif key == 'date_start' and sale_date < to_date(value):
            return False
        elif key == 'date_end' and sale_date > to_date(value):
            return False
        elif key == 'hour_start' and datetime_hour(sale['date_opened']) < value:
            return False
        elif key == 'hour_end' and datetime_hour(sale['date_opened']) > value:
            return False
    return True

def summary_dict_init(details):
    indicators = lambda: {'total': 0, 'max': 0, 'min': 0, 'quantity': 0, 'minutes': 0, 'diners': 0 }
    data = {'all': indicators()}
    for detail in details:
        if detail in details_allowed:
            data[detail] = defaultdict(indicators)
    return data

def add_data(indicators, sale):
    indicators['total'] += sale['total']
    indicators['max'] = max(indicators['max'], sale['total'])
    indicators['min'] = min(indicators['min'], sale['total']) if indicators['min'] != 0 else sale['total']
    indicators['quantity'] += 1
    indicators['diners'] += sale['diners']
    indicators['minutes'] += sale_duration_minutes(sale)

def to_date(date):
    return datetime.strptime(date, '%Y-%m-%d')

def to_datetime(date):
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

def datetime_hour(date):
    return int(date.split()[1].split(':')[0])

def sale_duration_minutes(sale):
    start = to_datetime(sale['date_opened'])
    end = to_datetime(sale['date_closed'])
    return (end - start).seconds // 60

def tables_by_zone(sales):
    zones = defaultdict(set)
    for sale in sales:
        table = int(sale['table'])
        zones[sale['zone']].add(int(sale['table']))
    return {zone: sorted(list(tables)) for zone, tables in zones.items()}

def tables_by_waiter(sales):
    waiters = defaultdict(set)
    for sale in sales:
        waiters[sale['waiter']].add(int(sale['table']))
    return {waiter: sorted(list(tables)) for waiter, tables in waiters.items()}

def num_days(filters):
    start, finish = to_date('2019-01-01'), to_date('2019-03-31')
    if 'date_start' in filters:
        start = to_date(filters['date_start'])
    if 'date_end' in filters:
        finish = to_date(filters['date_end'])
    return (finish - start).days + 1

def data_details(sales, filters, details_names):
    details = dict()
    details['names'] = details_names
    details['tables'] = tables_by_zone(sales)
    details['days'] = num_days(filters)
    
    return details
