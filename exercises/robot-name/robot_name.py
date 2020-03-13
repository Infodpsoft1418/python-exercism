import random
from string import ascii_uppercase

names_used = set()


class Robot:
    def __init__(self):
        self.name = self._create_name()

    def _make_letters(self):
        result = ""
        for i in range(2):
            result += ascii_uppercase[random.randint(0, 25)]
        return result

    def _make_numbers(self):
        result = ""
        for i in range(3):
            result += str(random.randint(0, 9))
        return result

    def _create_name(self):
        while True:
            name = f"{self._make_letters()}{self._make_numbers()}"
            if name not in names_used:
                names_used.add(name)
                return name

    def reset(self):
        self.name = self._create_name()
