from rna_transcription import to_rna


class TestRnaTranscription:
    def test_empty_rna_sequence(self):
        assert to_rna("") == ""

    def test_rna_complement_of_cytosine_is_guanine(self):
        assert to_rna("C") == "G"

    def test_rna_complement_of_guanine_is_cytosine(self):
        assert to_rna("G") == "C"

    def test_rna_complement_of_thymine_is_adenine(self):
        assert to_rna("T") == "A"

    def test_rna_complement_of_adenine_is_uracil(self):
        assert to_rna("A") == "U"

    def test_rna_complement(self):
        assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"
