#შეეცადეთ შექმნათ ფუნქცია, სადაც მომხმარებელი შეიყვანს რამე ორ არგუმენტს, მაგალითად "Goa" და Str, თქვენ უნდა შეამოწმოთ ემთხვევა თუ არა პირველი არგუმენტი მეორეს, ამ შემთხვევასი იქნება True რადგან "Goa" მართლაც არის String.

def func(x,y):
    if type(x)==y:
        return True
    else:
        return False
    
print(func("goa",str))