num = int(input("შეიყვანეთ რიცხვი: "))
if num % 2 == 0:
    print(f"{num} არის ლუწი")
else:
    print(f"{num} არის კენტი")

#2


numbers = []
for i in range(5):
    num = float(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)

print(f"რიცხვების ჯამი არის: {total}")
print(f"რიცხვების საშუალო არის: {average}")

