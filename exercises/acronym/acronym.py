import re


regex = re.compile(r"[A-Z]+['a-z]*|['a-z]+")


def abbreviate(words):
    return "".join(word[0].upper() for word in re.findall(regex, words))
