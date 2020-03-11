import pytest

from anagram import find_anagrams


class TestAnagram:
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        expected = []
        assert find_anagrams("diaper", candidates) == expected

    def test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        expected = ["stream", "maters"]
        assert find_anagrams("master", candidates) == expected

    def test_does_not_detect_anagram_subsets(self):
        candidates = ["dog", "goody"]
        expected = []
        assert find_anagrams("good", candidates) == expected

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        expected = ["inlets"]
        assert find_anagrams("listen", candidates) == expected

    def test_detects_three_anagrams(self):
        candidates = ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        expected = ["gallery", "regally", "largely"]
        assert find_anagrams("allergy", candidates) == expected

    def test_detects_multiple_anagrams_with_different_case(self):
        candidates = ["Eons", "ONES"]
        expected = ["Eons", "ONES"]
        assert find_anagrams("nose", candidates) == expected

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        candidates = ["last"]
        expected = []
        assert find_anagrams("mass", candidates) == expected

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        assert find_anagrams("Orchestra", candidates) == expected

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        expected = ["carthorse"]
        assert find_anagrams("Orchestra", candidates) == expected

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        assert find_anagrams("orchestra", candidates) == expected

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self):
        candidates = ["go Go GO"]
        expected = []
        assert find_anagrams("go", candidates) == expected

    def test_anagrams_must_use_all_letters_exactly_once(self):
        candidates = ["patter"]
        expected = []
        assert find_anagrams("tapper", candidates) == expected

    def test_words_are_not_anagrams_of_themselves_case_insensitive(self):
        candidates = ["BANANA", "Banana", "banana"]
        expected = []
        assert find_anagrams("BANANA", candidates) == expected

    def test_words_other_than_themselves_can_be_anagrams(self):
        candidates = ["Listen", "Silent", "LISTEN"]
        expected = ["Silent"]
        assert find_anagrams("LISTEN", candidates) == expected
