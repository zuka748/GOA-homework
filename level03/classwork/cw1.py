#1)  მომხმარებელს შემოატანინეთ სამი რიცხვი და გამოიტანეთ ამ რიცხვების ჯამი

num1=int(input("შემოიყვანე რიცხვი"))
num2=int(input("shemoiyvane meore ricxvi"))
num3=int(input("shemoiyvane mesame ricxvi"))
print(num1+num2+num3)

#შემოატანინეთ მომხმარებელს სახელი და შეინახეთ მისი სახელი ცვლადში

name=input("shemoiyvane saxeli")
print(name)

 #3 შემოიტანინეთ მომხმარელს ორი რიცხვი, თუ პირველი რიცხვი მეტია მეორეზეგამოიტანეთ True ( boolean ) თუარადა გამოიტანეთ False ( boolean )

num1=int(input("shemoiyvane ricxvi"))
num2=int(input("shemoiyvane meore ricxvi"))
if num1 > num2:
    print(True)
elif num1<num2:
    print(False)

 #4) მომხმარებელს შემოვატანინოთ სიტყვა და n რიცხვი, შემდეგ გამოვიტანოთ ეს სიტყვა n-ჯერ.

word=input("shemoiyvane sityva")
n=int(input("shemoitane ricxvi"))
print(word*n)

#5) შემოაყვანინეთ მომხმარებელს ორი რიცხვი, და გამოპრინტეთ ამ ორი რიცხვის გაერთიანებულ ვერსისას დამატებული 1, მაგ თუ ჯერ შემოვიდა ათი შემდეგ 11, თქვენი მიზანია გამოიტანოთ 1012, ვინაიდან 10 გაერთანებული 11 არის 1011 და 1011 + 1 არის 1012

num1=(input("shemoiyvane ricxvi"))
num2=(input("shemoitane meore ricxvi"))
final=num1+num2
result=int(final)+1
print(result)

