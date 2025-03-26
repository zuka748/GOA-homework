#1) მომხმარებელს შემოატანინეთ სიტყვა ან წინადადება შეინახეთ ის reversed_string შეტრიალებულად ცვლადში და გამოიტანეთ ეს ცვლადი

sityva=input("shemoitane sityva: ")
reversed_string=""
for i in sityva:
    reversed_string=i+reversed_string
    print(reversed_string)
    


#2) გამოთვალეთ 0 დან 100ს ჩათვლით ყველა რიცხვის ჯამი და შეინახეთ ის sum ცვლადში

sum=0
for i in range(1,101):
    sum+=i
    print(sum)
    


#3) მომხმარებეს შემოატანინეთ სამ ასოიანი სიტყვა, თუ  მან არ შემოიყვანა სამი ასო მაშინ გამოუპრინტეთ რომ მან უნდა შეიყვანოს ზუსტად სამი ასო და გაუშვას პროგრამა თავიდან. როდესაც მომხმარებელი შეიყვანს სამ ასოიან სიტყვას, შეამოწმეთ არის თუ არა ის პალინდრომი და გაოუტანეთ True ან False შესაბამისად

sityva=input("shemoiyvane 3 asoiani sityva")
if len(sityva)!=3:
    print("enter 3 letter")
    sityva=input("shemoiyvane 3 asoiani sityva")
elif len(sityva)==3:
    if sityva==sityva[::-1]:
        print(True)
    else:
        print(False)
 
    

#4) გამოიტანეთ 100დან 300მდე ყველა რიცხვის კვადრატი

for i in range(100,300):
    print(i**2)

#5) გამოიტანეთ ჯერ False, შემდეგ True, შემდეგ False, True, False... და ასე 1000-ჯერ

num=("true false")
print(num*1000)