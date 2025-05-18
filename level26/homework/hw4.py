# 5. შექმენით ფუნქცია სადაც მომხარებელი შეიყვანს რაიმე მათემატიკურ ოპერაციას და თქვენ უნდა დააბრუნოთ საბოლოო პასუხის type.

def func():
    z=input("sheiyvane matematikuri operacia")
    if type(func)==int:
        return "integer"
    if type(func)==str:
        return "string"
    if type(func)==bool:
        return "boolean"
    if type(func)==float:
        return "float"
print(func())
    

