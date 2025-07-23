#გამოიყენე for ციკლი და range(), რათა დაბეჭდო რიცხვები 1-იდან 10-ის ჩათვლით, ხოლო თითოეული რიცხვის შემდეგ დაბეჭდე მისი კვადრატი.

for i in range(1,11):
    print(i)
    print(i **2)


#მოცემულია სია: fruits = ["apple", "banana", "cherry", "mango"]. გამოიყენე for ციკლი, რათა დაბეჭდო ყველა ხილის სახელი დიდ ასოებით.

fruits=["apple", "banana", "cherry", "mango"]
for i in range(len(fruits)):
    print(fruits[i].upper())


#გამოიყენე while ციკლი და range() ფუნქციის მსგავსი ლოგიკა, რათა დაბეჭდო ყველა ლუწი რიცხვი 0-დან 20-ის ჩათვლით

num=0
while num<=20:
    print(num)
    num=num+2

#შექმენი სია numbers = [3, 7, 2, 9, 4, 1]. გამოიყენე for ციკლი, რათა იპოვო ამ სიაში მაქსიმალური რიცხვი (არ გამოიყენო max() ფუნქცია).

numbers = [3, 7, 2, 9, 4, 1]
res=0
for i in numbers:
    if i>res:
        res=i
print(res)



#5მომხმარებელს შეაყვანინე რიცხვი და გამოიყენე while ციკლი, რომელიც შეკრებს ამ რიცხვამდე ყველა მთელ რიცხვს (მაგ. თუ შეიყვანს 5-ს, უნდა დაითვალოს 1+2+3+4+5 = 15 და დაბეჭდოს შედეგი).
 
num = int(input("Enter any number: "))
i = 1
res = 0
while i <= num:
    res += i
    i += 1
print(res)
