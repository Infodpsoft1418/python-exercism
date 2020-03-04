from acronym import abbreviate


class TestAcronym:
    def test_basic(self):
        assert abbreviate("Portable Network Graphics") == "PNG"

    def test_lowercase_words(self):
        assert abbreviate("Ruby on Rails") == "ROR"

    def test_punctuation(self):
        assert abbreviate("First In, First Out") == "FIFO"

    def test_all_caps_word(self):
        assert abbreviate("GNU Image Manipulation Program") == "GIMP"

    def test_punctuation_without_whitespace(self):
        assert abbreviate("Complementary metal-oxide semiconductor") == "CMOS"

    def test_very_long_abbreviation(self):
        assert (
            abbreviate(
                "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
            )
            == "ROTFLSHTMDCOALM"
        )

    def test_consecutive_delimiters(self):
        assert abbreviate("Something - I made up from thin air") == "SIMUFTA"

    def test_apostrophes(self):
        assert abbreviate("Halley's Comet") == "HC"

    def test_underscore_emphasis(self):
        assert abbreviate("The Road _Not_ Taken") == "TRNT"
