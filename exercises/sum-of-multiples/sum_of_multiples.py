def is_multiple(i, multiples):
    for multiple in multiples:
        if multiple > 0 and i % multiple == 0:
            return True
    return False


def sum_of_multiples(limit, multiples):
    return sum(i for i in range(0, limit) if is_multiple(i, multiples))
