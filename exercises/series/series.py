def slices(series, length):
    if not 1 <= length <= len(series):
        raise ValueError
    return [series[i : i + length] for i in range(len(series) - length + 1)]
