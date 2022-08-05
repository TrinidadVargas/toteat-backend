from collections import defaultdict
from ..services import get_sales


def sales_by_day(args):
    data = get_sales()
    statistics = defaultdict(dict_init)

    for sale in data:
        day, time = sale['date_opened'].split()
        statistics[day]['total'] += sale['total']
        if 'waiter' in args:
            statistics[day]['waiter'][sale['waiter']] += sale['total']
        if 'cashier' in args:
            statistics[day]['cashier'][sale['cashier']] += sale['total']
        if 'zone' in args:
            statistics[day]['zone'][sale['zone']] += sale['total']
        if 'time' in args:
            if int(time.split(':')[0]) <= 16:
                statistics[day]['time']['lunch'] += sale['total']
            else:
                statistics[day]['time']['dinner'] += sale['total']
    
    return statistics

def dict_init():
    day = {
        'total': 0,
        'waiter': defaultdict(lambda: 0),
        'cashier': defaultdict(lambda: 0),
        'zone': defaultdict(lambda: 0),
        'time': {'lunch': 0, 'dinner': 0}
    }
    return day