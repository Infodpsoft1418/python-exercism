import re


class Luhn:
    def __init__(self, card_num):
        self._card_num = self._prepare(card_num)

    def _prepare(self, card_num):
        card_num = re.sub(r"[\s]*", "", card_num)
        return card_num

    def valid(self):
        if not re.fullmatch(r"[\d]{2,}", self._card_num):
            return False

        checking = [int(x) for x in self._card_num]
        sum_ = 0
        for num in checking[-2::-2]:
            x = num * 2
            if x > 9:
                x -= 9
            sum_ += x
        sum_ += sum(x for x in checking[-1::-2])
        return sum_ % 10 == 0
