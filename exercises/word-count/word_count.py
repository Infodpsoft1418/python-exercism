from collections import Counter
import re

WORDS = re.compile(r"[a-z0-9]+(['][a-z]+)?")


def count_words(sentence):
    return Counter(match.group(0) for match in WORDS.finditer(sentence.lower()))
