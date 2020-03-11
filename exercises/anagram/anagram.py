def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if _sorted(word) == _sorted(candidate) and word.lower() != candidate.lower():
            result.append(candidate)
    return result


def _sorted(word):
    return sorted(word.lower())
