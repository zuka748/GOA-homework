#1) მომხმარებელს შემოაყვანინეთ რიცხვი. თუ ის ლუწია გამოიტანეთ სიტყვა **"ლუწი"**, ხოლო თუ კენტია გამოიტანეთ **"კენტი"**.
 
num1=int(input("shemoiyvane ricxvi"))
if num1 %2==0 :
    print("even")
elif num1 %2==1 :
    print("odd")

 #2) შეამოწმეთ მომხმარებლის შემოყვანილი რიცხვი ნეგატიურია პოზიტიურია თუ 0-ია. ამის მიხედვით გაუტოლეთ ცვლად *res* 0, -1 ან 1.

num1=int(input("shemoiyvane ricxvi"))
if num1==0 :
   print("udris 0")
elif num1>0 :
    print("metia 0ze")
elif num1<0:
    print("naklebia 0ze")


#3) მომხმარებლს შემოატანინეთ 2 რიცხვი და გამოიტანეთ უდიდესი ტერმინალში.

num1=int(input("shemoitane ricxvi"))
num2=int(input("shemoitane meore ricxvi"))
if num1>num2:
    print(num1>num2)
elif num1<num2 :
    print(num2>num1)


    
