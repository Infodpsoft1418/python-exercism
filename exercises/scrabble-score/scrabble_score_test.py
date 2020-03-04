from scrabble_score import score


class TestScrabbleScore:
    def test_lowercase_letter(self):
        assert score("a") == 1

    def test_uppercase_letter(self):
        assert score("A") == 1

    def test_valuable_letter(self):
        assert score("f") == 4

    def test_short_word(self):
        assert score("at") == 2

    def test_short_valuable_word(self):
        assert score("zoo") == 12

    def test_medium_word(self):
        assert score("street") == 6

    def test_medium_valuable_word(self):
        assert score("quirky") == 22

    def test_long_mixed_case_word(self):
        assert score("OxyphenButazone") == 41

    def test_english_like_word(self):
        assert score("pinata") == 8

    def test_empty_input(self):
        assert score("") == 0

    def test_entire_alphabet_available(self):
        assert score("abcdefghijklmnopqrstuvwxyz") == 87
