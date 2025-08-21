def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) 


#4
n = int(input("შეიყვანეთ რიგების რაოდენობა"))
for i in range(1, n + 1):
    print("*" * i)

