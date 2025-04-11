#1
def res(num):
    x=0
    for i in str(num):
        x+=int(i)
    return num % x
print(res(120))


#2

num=int(input("sheiyvane ricxvi"))
if num % 2 !=0:
    num+=1
print("ricxvi",num)


#3
num=int(input("ricxvi"))
if num % 2==0:
    print(num+5)
else:
    num*3
nashti= num%5
print("nashti 5ze gayofisas",nashti)

#4 f''-ის გამოყენებით შექმენიტ ერთი დიდი ტექსტი სადაც შევა მომხმარებლის მიერ შეყვანილი: სახელი, გვარი, ასაკი, ქვეყანა

name=input("zuka")
surname=input("bichoshvili")
age=int(input(15))
country=input("georgia")
print(f'gamarjoba me var{name}{surname},var{age}wlis da vcxovrob {country}-shi')


# 5

#მე მირჩევნია f''სტრინგით რადგან ყველაზე მოსახერხებელია მას აქვს ბევრი უპირატესობა არის მარტივი და სწრაფად იკითხება შეგიძლიათ ცვლადებიც და გამოთვლებიც ჩაწეროთ {}-ში.