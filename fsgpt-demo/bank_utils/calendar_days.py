"""Business day helpers for settlement dates."""
from datetime import date, timedelta

HOLIDAYS = {date(2026, 3, 23), date(2026, 8, 14), date(2026, 12, 25)}


def is_business_day(d):
    """Monday to Friday and not a listed holiday."""
    return d.weekday() < 5 and d not in HOLIDAYS


def add_business_days(start, days):
    """The date that is a number of business days after start."""
    d = start
    while days > 0:
        d += timedelta(days=1)
        if is_business_day(d):
            days -= 1
    return d


def business_days_between(start, end):
    """Number of business days from start up to end."""
    count = 0
    d = start
    while d < end:
        if is_business_day(d):
            count += 1
        d += timedelta(days=1)
    return count
