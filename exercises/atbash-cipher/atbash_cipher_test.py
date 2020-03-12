from atbash_cipher import decode, encode


class TestAtbashCipher:
    def test_encode_yes(self):
        assert encode("yes") == "bvh"

    def test_encode_no(self):
        assert encode("no") == "ml"

    def test_encode_omg(self):
        assert encode("OMG") == "lnt"

    def test_encode_spaces(self):
        assert encode("O M G") == "lnt"

    def test_encode_mindblowingly(self):
        assert encode("mindblowingly") == "nrmwy oldrm tob"

    def test_encode_numbers(self):
        assert encode("Testing,1 2 3, testing.") == "gvhgr mt123 gvhgr mt"

    def test_encode_deep_thought(self):
        assert encode("Truth is fiction.") == "gifgs rhurx grlm"

    def test_encode_all_the_letters(self):
        assert (
            encode("The quick brown fox jumps over the lazy dog.")
            == "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        )

    def test_decode_exercism(self):
        assert decode("vcvix rhn") == "exercism"

    def test_decode_a_sentence(self):
        assert (
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v")
            == "anobstacleisoftenasteppingstone"
        )

    def test_decode_numbers(self):
        assert decode("gvhgr mt123 gvhgr mt") == "testing123testing"

    def test_decode_all_the_letters(self):
        assert (
            decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")
            == "thequickbrownfoxjumpsoverthelazydog"
        )

    def test_decode_with_too_many_spaces(self):
        assert decode("vc vix    r hn") == "exercism"

    def test_decode_with_no_spaces(self):
        assert (
            decode("zmlyhgzxovrhlugvmzhgvkkrmthglmv")
            == "anobstacleisoftenasteppingstone"
        )
