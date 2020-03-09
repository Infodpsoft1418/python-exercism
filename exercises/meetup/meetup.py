from datetime import date, timedelta


class MeetupDayException(Exception):
    pass


DAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def get_teenth(year, month, day_of_week):
    d = date(year, month, 13)
    while d.day < 20:
        if d.weekday() == DAYS[day_of_week]:
            return d
        d += timedelta(days=1)
    raise MeetupDayException


def get_nth(nth, year, month, day_of_week):
    d = date(year, month, 1)
    n = 0
    while d.month == month:
        if d.weekday() == DAYS[day_of_week]:
            n += 1
            if n == nth:
                return d
        d += timedelta(days=1)
    raise MeetupDayException


def get_last(year, month, day_of_week):
    d = date(year, month, 21)
    possible_last = None
    while d.month == month:
        if d.weekday() == DAYS[day_of_week]:
            possible_last = d
        d += timedelta(days=1)
    if possible_last:
        return possible_last
    raise MeetupDayException


def meetup(year, month, week, day_of_week):
    if week == "teenth":
        return get_teenth(year, month, day_of_week)
    elif week == "1st":
        return get_nth(1, year, month, day_of_week)
    elif week == "2nd":
        return get_nth(2, year, month, day_of_week)
    elif week == "3rd":
        return get_nth(3, year, month, day_of_week)
    elif week == "4th":
        return get_nth(4, year, month, day_of_week)
    elif week == "5th":
        return get_nth(5, year, month, day_of_week)
    elif week == "last":
        return get_last(year, month, day_of_week)
    raise MeetupDayException
