#**1.** შექმენით პროგრამა სადაც მომხმარებელი შემოიყვანს ასაკს და თქვენ უნდა გაარკვიოთ, უნდა იაროს მან ბაღში, სკოლაში თუ სამსახურში: თუ ასაკი მეტი იქნება 2-ზე == ბაღი | თუ ასაკი მეტია ან უდრის 6-ს == სკოლაში | დანარჩენ შემთხვევაში სამსახური.

num1=int(input("sheni asaki"))
if num1>2 :
    print("bagi")
elif num1>=6 :
    print("skola")
else:
    print("samsaxuri")

#**2.** შექმენით პროგრამა რომელშიც: მომხმარებელს შემოყავს ინფორმაცია თუ რომელ პროგრამირების  აკადემიაში დადის, თუ მან შეიყვანა "Goa", გამოიტანეთ "U r a real chad!", ხოლო დანარჩენ შემთხვევაში "Join Goa, become a chad".

academy=input("romel akademiashi dadixar")
if academy=="goa":
    print("u r a real chad")
else:
    print("join goa become a chad")

#**3.** მომხმარებელს შემოყავს პროექტში მიღებული ქულის შესახებ, თუ ის 90-ზე მეტია შეფასებაა A, თუ 75-ზე მეტია შეფასებაა B, თუ 60-ზე მეტია შეფასებაა C, თუ 50-ზე მეტია შეფასებაა D, თუ 40-ზე E და თუ 30-ზე F, Good Luck💚

num1=int(input("shemoiyvane raime qula"))
if num1>90:
    print("A")
elif num1>75:
    print("B")
elif num1>60:
    print("C")
elif num1>50:
    print("D")
elif num1>40:
    print("E")
elif num1>30:
    print("F")
    

