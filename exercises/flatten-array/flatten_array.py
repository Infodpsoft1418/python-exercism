def flatten(iterable):
    result = []
    for i in iterable:
        if i is None:
            continue
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
