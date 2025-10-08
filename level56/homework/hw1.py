def most_frequent_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    most_common = max(freq, key=freq.get)
    return most_common
print(most_frequent_char("banana")) 
