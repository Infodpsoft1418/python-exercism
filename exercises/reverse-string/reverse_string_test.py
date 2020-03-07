from reverse_string import reverse


class TestReverseString:
    def test_an_empty_string(self):
        assert reverse("") == ""

    def test_a_word(self):
        assert reverse("robot") == "tobor"

    def test_a_capitalized_word(self):
        assert reverse("Ramen") == "nemaR"

    def test_a_sentence_with_punctuation(self):
        assert reverse("I'm hungry!") == "!yrgnuh m'I"

    def test_a_palindrome(self):
        assert reverse("racecar") == "racecar"

    def test_an_even_sized_word(self):
        assert reverse("drawer") == "reward"
