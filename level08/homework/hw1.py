#4For loop-ის დახმარებით შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს რიცხვს (50-ის ჩათვლით, თუ არა დაუპრინტეთ, რომ თავიდან შეიყვანოს), და თქვენ გამოიტანეთ ამ რიცხვის ჯერადები 100-ის ჩათვლით.

num= int(input("sheiyvane ricxvi (50is chatvlit):"))
if num>50:
    print("arasworia")
for i in range(num, 101, num):
        print(i)

# 5. შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას (ოთხნიშნა integer-რიცხვი), და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)

num=(1000,9999)
while True:
      gamoicani=int(input("gamoicani otxnishna ricxi:"))
      if gamoicani==num:
            print("sworiaa")
            break
      print("arasworia scade xelaxla")




