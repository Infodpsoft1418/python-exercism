import pytest

from series import slices


class TestSeries:
    def test_slices_of_one_from_one(self):
        assert slices("1", 1) == ["1"]

    def test_slices_of_one_from_two(self):
        assert slices("12", 1) == ["1", "2"]

    def test_slices_of_two(self):
        assert slices("35", 2) == ["35"]

    def test_slices_of_two_overlap(self):
        assert slices("9142", 2) == ["91", "14", "42"]

    def test_slices_can_include_duplicates(self):
        assert slices("777777", 3) == ["777", "777", "777", "777"]

    def test_slices_of_a_long_series(self):
        assert slices("918493904243", 5) == [
            "91849",
            "18493",
            "84939",
            "49390",
            "93904",
            "39042",
            "90424",
            "04243",
        ]

    def test_slice_length_is_too_large(self):
        with pytest.raises(ValueError):
            slices("12345", 6)

    def test_slice_length_cannot_be_zero(self):
        with pytest.raises(ValueError):
            slices("12345", 0)

    def test_slice_length_cannot_be_negative(self):
        with pytest.raises(ValueError):
            slices("123", -1)

    def test_empty_series_is_invalid(self):
        with pytest.raises(ValueError):
            slices("", 1)
