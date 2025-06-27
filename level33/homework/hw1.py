def manual_split(string, delimiter=' '):
    result = []
    current = ''
    
    for char in string:
        if char == delimiter:
            if current != '':
                result.append(current)
                current = ''
        else:
            current += char
    if current:
        result.append(current)

    return result
