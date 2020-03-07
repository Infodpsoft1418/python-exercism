from isbn_verifier import is_valid


class TestIsbnVerifier:
    def test_valid_isbn_number(self):
        assert is_valid("3-598-21508-8")

    def test_invalid_isbn_check_digit(self):
        assert not is_valid("3-598-21508-9")

    def test_valid_isbn_number_with_a_check_digit_of_10(self):
        assert is_valid("3-598-21507-X")

    def test_check_digit_is_a_character_other_than_x(self):
        assert not is_valid("3-598-21507-A")

    def test_invalid_character_in_isbn(self):
        assert not is_valid("3-598-P1581-X")

    def test_x_is_only_valid_as_a_check_digit(self):
        assert not is_valid("3-598-2X507-9")

    def test_valid_isbn_without_separating_dashes(self):
        assert is_valid("3598215088")

    def test_isbn_without_separating_dashes_and_x_as_check_digit(self):
        assert is_valid("359821507X")

    def test_isbn_without_check_digit_and_dashes(self):
        assert not is_valid("359821507")

    def test_too_long_isbn_and_no_dashes(self):
        assert not is_valid("3598215078X")

    def test_too_short_isbn(self):
        assert not is_valid("00")

    def test_isbn_without_check_digit(self):
        assert not is_valid("3-598-21507")

    def test_check_digit_of_x_should_not_be_used_for_0(self):
        assert not is_valid("3-598-21515-X")

    def test_empty_isbn(self):
        assert not is_valid("")

    def test_input_is_9_characters(self):
        assert not is_valid("134456729")

    def test_invalid_characters_are_not_ignored(self):
        assert not is_valid("3132P34035")

    def test_input_is_too_long_but_contains_a_valid_isbn(self):
        assert not is_valid("98245726788")
