# 1. შემოატანინეთ მომხმარებელს თავისი ასაკი და შეამოწმეთ, თუ ის 10-წლისაა ან უფრო პატარა, დაპრინტეთ "Kid", თუ 10-ზე მეტი და 18-ზე ნაკლები გამოიტანეთ "teenager", თუ 18-ზე მეტია და 30-ზე ნაკლები "adult", სხვა შემთხვევაში "unc"

age=int(input("asaki"))
if age <=10:
    print("kid", end="")
elif age > 10 and age <18:
    print("teenager",end="")
elif age >=18 and age < 30:
    print("adult", end="")
else:
    print("adult", end="")
