#1
def get_count(sentence):
    count=0
    vowel="aeiou"
    for i in sentence:
        if i in vowel:
            count+=1
    return count

#6
def descending_order(num):
    return int( "".join(sorted(str(num),reverse=True)))

#7
def square_digits(num):
    result = ""
    for digit in str(num):
        squared = int(digit) ** 2
        result += str(squared)
    return int(result)