#1) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-დან 10-მდე
for i in range(1,10):
    print(i)

#2)for ციკლის გამოყენებით გამოიტანეთ რიცხვები 5-დან 25-მდე

for i in range(5,25):
    print(i)

#3)for ციკლის გამოყენებით გამოიტანეთ რიცხვები 10-დან 100-მდე, 5ის stepით
for i in range(10,100,5):
    print(i)

#4)მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი

shemoiyvane_sityva=input("sityva")
for i in shemoiyvane_sityva:
    if i =="A":
        print(i)
    else:
        print("")


#5)კომენტარებით დაწერეთ რას გამოიტანს შემდეგი გამოსახულება: True or True and False or True and False and False and True or False


True or True and False or True and False and False and True or False==False
       
