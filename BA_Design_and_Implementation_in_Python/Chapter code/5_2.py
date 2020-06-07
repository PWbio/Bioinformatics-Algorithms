"""Naive Algorithm for Fixed Pattern Finding"""

def search_first_pattern(seq, pattern):
    """Return the offset position of the first pattern found."""
    found = False
    i = 0
    while i <= len(seq) - len(pattern) and not found:
        # i specify starting position in input seq to match with pattern.
        j = 0
        while j < len(pattern) and pattern[j] == seq[i + j]:
            # j define the position of the pattern.
            # 'While' loop will match seq and pattern one by one.
            j = j + 1
        if j == len(pattern):
            # If seq and pattern are identical, j == len (pattern).
            # Otherwise, j < len(pattern).
            found = True
        else:
            i += 1
    if found:
        return i
    else:
        return -1


def search_all_pattern(seq, pattern):
    """Return the offset position of all patterns found. [List]"""
    res = []
    for i in range(len(seq) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and pattern[j] == seq[i + j]:
            j = j + 1
        if j == len(pattern):
            res.append(i)
    return res


"""The input sequence and pattern are case sensitive."""