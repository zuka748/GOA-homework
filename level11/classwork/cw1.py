#1  
def make_negative(number):
    if number<=0:
        return number
    return int(f"-{number}")

#2
def solution(string):
    res=""
    for i in string:
        res=i+res
        return res

#3  
def number_to_string(num):
    return str(num)
