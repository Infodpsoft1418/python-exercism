import pytest

from hamming import distance


class TestHamming:
    def test_empty_strands(self):
        assert distance("", "") == 0

    def test_single_letter_identical_strands(self):
        assert distance("A", "A") == 0

    def test_single_letter_different_strands(self):
        assert distance("G", "T") == 1

    def test_long_identical_strands(self):
        assert distance("GGACTGAAATCTG", "GGACTGAAATCTG") == 0

    def test_long_different_strands(self):
        assert distance("GGACGGATTCTG", "AGGACGGATTCT") == 9

    def test_disallow_first_strand_longer(self):
        with pytest.raises(RuntimeError):
            distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with pytest.raises(RuntimeError):
            distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with pytest.raises(RuntimeError):
            distance("", "G")

    def test_disallow_right_empty_strand(self):
        with pytest.raises(RuntimeError):
            distance("G", "")
