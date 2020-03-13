from space_age import SpaceAge


class TestSpaceAge:
    def test_age_on_earth(self):
        assert SpaceAge(1000000000).on_earth() == 31.69

    def test_age_on_mercury(self):
        assert SpaceAge(2134835688).on_mercury() == 280.88

    def test_age_on_venus(self):
        assert SpaceAge(189839836).on_venus() == 9.78

    def test_age_on_mars(self):
        assert SpaceAge(2129871239).on_mars() == 35.88

    def test_age_on_jupiter(self):
        assert SpaceAge(901876382).on_jupiter() == 2.41

    def test_age_on_saturn(self):
        assert SpaceAge(2000000000).on_saturn() == 2.15

    def test_age_on_uranus(self):
        assert SpaceAge(1210123456).on_uranus() == 0.46

    def test_age_on_neptune(self):
        assert SpaceAge(1821023456).on_neptune() == 0.35
