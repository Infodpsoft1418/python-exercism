def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise RuntimeError("The two strands must be the same length")
    total = 0
    for i, piece_a in enumerate(strand_a):
        if piece_a != strand_b[i]:
            total += 1
    return total
