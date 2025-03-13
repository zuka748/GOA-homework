#1 მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით, გამოთვალეთ და გამოიტანეთ მხოლოდ კენტი რიცხვების ჯამი

num=int(input("shemoiyvane ricxvi: "))
count=0
for i in range(1,num+1,2) :
    count+=i
print("sum of odd numbers:",count)
      

#2)მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით გამოიტანეთ მხოლოდ ის რიცხვები, რომლებზეც უნაშთოდ იყოფა შემოტანილი რიცხვი

num=int(input("enter number: "))
for i in range(2,num):
    if num %i==0:
     print(i)


#3)კლასში დაწერილ კოდს დაამატეთ ლოგიკა, რომ 3 არასწორი პაროლის შეყვანის შემდეგ კოდი გაჩერდეს

sheiyvane_paroli=input("paroli")
correct_password="zuka123"
while sheiyvane_paroli!=correct_password:
   sheiyvane_paroli=input("sheiyvane paroli")
   if sheiyvane_paroli==correct_password:
      print("sworia")
#4მომხმარებელს შემოატანინეთ რაიმე stringი და for ციკლის გამოყენებით დააბრუნეთ ეს სტრინგი შემოტრიალებული

