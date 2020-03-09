from run_length_encoding import encode, decode


class TestRunLengthEncoding:
    def test_encode_empty_string(self):
        assert encode("") == ""

    def test_encode_single_characters_only_are_encoded_without_count(self):
        assert encode("XYZ") == "XYZ"

    def test_encode_string_with_no_single_characters(self):
        assert encode("AABBBCCCC") == "2A3B4C"

    def test_encode_single_characters_mixed_with_repeated_characters(self):
        assert (
            encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
            == "12WB12W3B24WB"
        )

    def test_encode_multiple_whitespace_mixed_in_string(self):
        assert encode("  hsqq qww  ") == "2 hs2q q2w2 "

    def test_encode_lowercase_characters(self):
        assert encode("aabbbcccc") == "2a3b4c"

    def test_decode_empty_string(self):
        assert decode("") == ""

    def test_decode_single_characters_only(self):
        assert decode("XYZ") == "XYZ"

    def test_decode_string_with_no_single_characters(self):
        assert decode("2A3B4C") == "AABBBCCCC"

    def test_decode_single_characters_with_repeated_characters(self):
        assert (
            decode("12WB12W3B24WB")
            == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
        )

    def test_decode_multiple_whitespace_mixed_in_string(self):
        assert decode("2 hs2q q2w2 ") == "  hsqq qww  "

    def test_decode_lower_case_string(self):
        assert decode("2a3b4c") == "aabbbcccc"

    def test_encode_followed_by_decode_gives_original_string(self):
        assert decode(encode("zzz ZZ  zZ")) == "zzz ZZ  zZ"
