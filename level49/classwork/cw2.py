def scramble(strng, array):
    result = [""] * len(strng)   # create empty list with same length
    for char, idx in zip(strng, array):
        result[idx] = char
    return "".join(result)
