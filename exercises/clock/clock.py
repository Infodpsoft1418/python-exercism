class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self._correct_clock()

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        return self._correct_clock()

    def __sub__(self, minutes):
        self.minute -= minutes
        return self._correct_clock()

    def _correct_clock(self):
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24
        return self
