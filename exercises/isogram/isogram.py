import re


def is_isogram(string):
    string = re.sub(r"[\-\s]+", "", string)
    string = string.lower()
    return len(set(string)) == len(string)
