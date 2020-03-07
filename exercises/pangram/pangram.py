import re

NONLETTERS = re.compile(r"[\W\d_]*")


def is_pangram(sentence):
    sentence = NONLETTERS.sub("", sentence)
    return len(set(sentence.lower())) == 26
