#1
def square_digits(num):
    result = ""
    for digit in str(num):
        squared = int(digit) ** 2
        result += str(squared)
    return int(result)

#2
def get_min_max(seq):
    return (min(seq), max(seq))