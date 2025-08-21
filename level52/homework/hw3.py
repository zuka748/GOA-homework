numbers = [4, 7, 1, 9, 2]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("ყველაზე დიდი რიცხვი არის:", largest)


#6
word = input("შეიყვანეთ სიტყვა: ")
shemotrialebuli = word[::-1]
if word == shemotrialebuli:
    print('არის პალინდრომი')
else:
    print('არაა პალინდრომი.')
