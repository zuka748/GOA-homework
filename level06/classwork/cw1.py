#1მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ for ციკლის გამოყენებით შეამოწმეთ, არის თუ არა ეს რიცხვი მარტივი, თუ არის დაპრინტეთ "your number is a prime" თუ არ არის დაპრინტეთ "your number is not a prime

num=int(input("shemoitane ricxvi: "))

if num>1 :
    is_prime=True
    for i in range(2,num):
        if num % i==0:
            is_prime=False
            break

if is_prime:
    print("your number is a prime")
else:
    print("your number is not a prime")