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
        statistics[key]['total'] += sale['total']
        if 'waiter' in args:
            statistics[key]['waiter'][sale['waiter']] += sale['total']
        if 'cashier' in args:
            statistics[key]['cashier'][sale['cashier']] += sale['total']
        if 'zone' in args:
            statistics[key]['zone'][sale['zone']] += sale['total']
        if 'time' in args:
            if int(time.split(':')[0]) <= 16:
                statistics[key]['time']['lunch'] += sale['total']
            else:
                statistics[key]['time']['dinner'] += sale['total']
    
    return list(statistics.values())

def dict_init():
    day = {
        'total': 0,
        'waiter': defaultdict(lambda: 0),
        'cashier': defaultdict(lambda: 0),
        'zone': defaultdict(lambda: 0),
        'time': {'lunch': 0, 'dinner': 0}
    }
    return day