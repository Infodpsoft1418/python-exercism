DNA_TO_RNA = {
    "C": "G",
    "G": "C",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand):
    return "".join(DNA_TO_RNA[n] for n in dna_strand)
