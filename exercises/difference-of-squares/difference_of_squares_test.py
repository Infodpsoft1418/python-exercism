from difference_of_squares import difference_of_squares, square_of_sum, sum_of_squares


class TestDifferenceOfSquares:
    def test_square_of_sum_1(self):
        assert square_of_sum(1) == 1

    def test_square_of_sum_5(self):
        assert square_of_sum(5) == 225

    def test_square_of_sum_100(self):
        assert square_of_sum(100) == 25502500

    def test_sum_of_squares_1(self):
        assert sum_of_squares(1) == 1

    def test_sum_of_squares_5(self):
        assert sum_of_squares(5) == 55

    def test_sum_of_squares_100(self):
        assert sum_of_squares(100) == 338350

    def test_difference_of_squares_1(self):
        assert difference_of_squares(1) == 0

    def test_difference_of_squares_5(self):
        assert difference_of_squares(5) == 170

    def test_difference_of_squares_100(self):
        assert difference_of_squares(100) == 25164150
