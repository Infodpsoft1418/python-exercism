import re


def is_valid(isbn):
    isbn = re.sub(r"[\-]*", "", isbn)
    if len(isbn) != 10:
        return False

    lst = []
    countdown = 10
    for i, n in enumerate(isbn):
        if i == 9 and n == "X":
            lst.append(10 * countdown)
        else:
            try:
                lst.append(int(n) * countdown)
            except ValueError:
                return False
        countdown -= 1
    return sum(lst) % 11 == 0
