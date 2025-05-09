def who_is_paying(name):
    result = []
    for i in name:
        if len(name) <= 2:
            result.append([name])
        else:
            result.append([name, name[:2]])
    return result
print( who_is_paying)