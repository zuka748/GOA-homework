#1
def repeat_str(repeat, string):
    return (repeat*string)

#2
def say_hello(name):
    return "Hello,"+" "+name

#3
def rps(p1, p2):
     if p1 == p2:
         return "Draw!"
     elif p1 == 'rock' and p2 == 'scissors':
         return "Player 1 won!"
     elif p1 == 'scissors' and p2 == 'paper':
         return "Player 1 won!"
     elif p1 == 'paper' and p2 == 'rock':
         return "Player 1 won!"
     else:
         return "Player 2 won!"
     

#4

def get_grade(s1, s2, s3):
    average = (s1+s2+s3) /3
    if average >=90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"
    
#5

def simple_multiplication(number) :
    if number %2==0:
        return number *8
    else:
        return number*9
    

