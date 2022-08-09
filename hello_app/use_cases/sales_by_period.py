from collections import defaultdict
from datetime import datetime
from ..services import get_sales

day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def sales_by_period(args):
    data = get_sales()
    statistics = dict()
    statistics['day'] = sales_by_specific_period(data, args, period='day')
    statistics['month'] = sales_by_specific_period(data, args, period='month')
    statistics['weekday'] = sales_by_specific_period(data, args, period='weekday')

    return statistics

def sales_by_specific_period(data, args, period='day'):
    statistics = defaultdict(dict_init)

    for sale in data:
        day, time = sale['date_opened'].split()
        if period == 'day': key = day
        elif period == 'month': key = months[int(day.split('-')[1]) - 1]
        elif period == 'weekday': key = day_of_the_week[datetime.strptime(day, '%Y-%m-%d').weekday()]

        statistics[key]['date'] = key
        add_data(statistics[key]['all'], sale)
        if 'waiter' in args:
            add_data(statistics[key]['waiter'][sale['waiter']], sale)
        if 'cashier' in args:
            add_data(statistics[key]['cashier'][sale['cashier']], sale)
        if 'zone' in args:
            add_data(statistics[key]['zone'][sale['zone']], sale)
        if 'time' in args:
            if int(time.split(':')[0]) <= 16:
                add_data(statistics[key]['time']['lunch'], sale)
            else:
                add_data(statistics[key]['time']['dinner'], sale)
    
    return list(statistics.values())

def add_data(indicators, sale):
    indicators['total'] += sale['total']
    indicators['max'] = max(indicators['max'], sale['total'])
    indicators['min'] = min(indicators['min'], sale['total']) if indicators['min'] != 0 else sale['total']
    indicators['num_sales'] += 1

def dict_init():
    indicators = lambda: {'total': 0, 'max': 0, 'min': 0, 'num_sales': 0}
    # tiempo 
    day = {
        'all': indicators() ,
        'waiter': defaultdict(lambda: indicators()),
        'cashier': defaultdict(lambda: indicators()),
        'zone': defaultdict(lambda: indicators()),
        'time': defaultdict(lambda: indicators())
    }
    return day