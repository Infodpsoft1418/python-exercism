from pangram import is_pangram


class TestPangram:
    def test_empty_sentence(self):
        assert not is_pangram("")

    def test_perfect_lower_case(self):
        assert is_pangram("abcdefghijklmnopqrstuvwxyz")

    def test_only_lower_case(self):
        assert is_pangram("the quick brown fox jumps over the lazy dog")

    def test_missing_the_letter_x(self):
        assert not is_pangram(
            "a quick movement of the enemy will jeopardize five gunboats"
        )

    def test_missing_the_letter_h(self):
        assert not is_pangram("five boxing wizards jump quickly at it")

    def test_with_underscores(self):
        assert is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog")

    def test_with_numbers(self):
        assert is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs")

    def test_missing_letters_replaced_by_numbers(self):
        assert not is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog")

    def test_mixed_case_and_punctuation(self):
        assert is_pangram('"Five quacking Zephyrs jolt my wax bed."')

    def test_case_insensitive(self):
        assert not is_pangram("the quick brown fox jumps over with lazy FX")
