from armstrong_numbers import is_armstrong_number


class TestArmstrongNumbers:
    def test_zero_is_an_armstrong_number(self):
        assert is_armstrong_number(0)

    def test_single_digit_numbers_are_armstrong_numbers(self):
        assert is_armstrong_number(5)

    def test_there_are_no_2_digit_armstrong_numbers(self):
        assert not is_armstrong_number(10)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        assert is_armstrong_number(153)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        assert not is_armstrong_number(100)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        assert is_armstrong_number(9474)

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        assert not is_armstrong_number(9475)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        assert is_armstrong_number(9926315)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        assert not is_armstrong_number(9926314)
