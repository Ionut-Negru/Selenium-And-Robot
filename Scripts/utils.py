
import datetime


def compare_date(date1=None, date2=None):
    if date1 == date2:
        return '0'
    elif date1 < date2:
        return '-1'
    elif date1 > date2:
        return '1'