import datetime

GIGASECOND = datetime.timedelta(seconds=10 ** 9)


def add(moment):
    return moment + GIGASECOND
