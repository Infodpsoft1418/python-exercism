EARTH_SECONDS = 31557600


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def period(self, year):
        return round(self.seconds / (year * EARTH_SECONDS), 2)

    def on_mercury(self):
        return self.period(0.2408467)

    def on_venus(self):
        return self.period(0.61519726)

    def on_earth(self):
        return self.period(1.0)

    def on_mars(self):
        return self.period(1.8808158)

    def on_jupiter(self):
        return self.period(11.862615)

    def on_saturn(self):
        return self.period(29.447498)

    def on_uranus(self):
        return self.period(84.016846)

    def on_neptune(self):
        return self.period(164.79132)
