def is_vow(inp):
    result = []
    for num in inp:
        char = chr(num)
        if char in 'aeiou':
            result.append(char)
        else:
            result.append(num)
    return result