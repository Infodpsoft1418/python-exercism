import pytest

from rotational_cipher import rotate


class TestRotationalCipher:
    def test_rotate_a_by_0_same_output_as_input(self):
        assert rotate("a", 0) == "a"

    def test_rotate_a_by_1(self):
        assert rotate("a", 1) == "b"

    def test_rotate_a_by_26_same_output_as_input(self):
        assert rotate("a", 26) == "a"

    def test_rotate_m_by_13(self):
        assert rotate("m", 13) == "z"

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        assert rotate("n", 13) == "a"

    def test_rotate_capital_letters(self):
        assert rotate("OMG", 5) == "TRL"

    def test_rotate_spaces(self):
        assert rotate("O M G", 5) == "T R L"

    def test_rotate_numbers(self):
        assert rotate("Testing 1 2 3 testing", 4) == "Xiwxmrk 1 2 3 xiwxmrk"

    def test_rotate_punctuation(self):
        assert rotate("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"

    def test_rotate_all_letters(self):
        assert (
            rotate("The quick brown fox jumps over the lazy dog.", 13)
            == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
        )
