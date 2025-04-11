def calculator(x, y, op):
    if type(x)==int and type(y)==int:
        if op=="+":
            return x+y
        if op=="-":
            return x-y
        if op=="*":
            return x*y
        if op=="/":
            return x/y
        else:
            "unknown value"



#2

def string_clean(s):
    to_remove='0123456789'
    result=""
    for i in s:
        if i not in to_remove:
            result+=i
    return result

#3
def count_char_occurrences(string, char):
    count=0
    for i in string:
        if i ==char:
            count+=1
    return count

#4

 