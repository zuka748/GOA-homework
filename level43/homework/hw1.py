#1
def no_space(x):
    return ''.join(x.split())

#2
def abbrev_name(name):
    splited=name.split(" ")
    return splited[0][0].upper()+"."+splited[1][0].upper()

#3
def double_integer(i):
    return i*2

#4
def repeat_str(repeat, string):
    return string*repeat

#5
def remove_char(s):
    return s[1:-1]