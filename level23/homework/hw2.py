#შექმენით ფუნქცია სადაც მომხარებელი გასაცემს ასევე ორ არგუმენტს, თქვენი დავალებაა რომ უფრო დიდი რიცხვი გაყოთ უფრო პატარაზე (ასევე არ იცით რა მონაცმეთა ტიპია), თუ გამყოფი აღმოჩნდება 0 გამოიტანეთ ZeroDivissionError

def func(num1, num2):
    if num1>num2 and type(num1)==int and type(num2)==int:
        if num2==0:
            return "ZeroDivissionError"
        else:
            return num1/num2
    else:
        return "incorrect input"
print(func("5","3"))