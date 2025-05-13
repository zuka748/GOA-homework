# 2. შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან არგუმენტს და მისი type-ის სესაბამისად გამოიტანეთ სიტყვები:
# Str - "Literature"
# Int/Float - "Math"
# Bool - "Science"


def func(x,y):
    if type(x) and type(y)==str:
        return "Literature"
    if type(x) and type(y)==int:
        return "Math"
    if type(x) and type(y)==float:
        return "Math"
    if type(x) and type(y)==bool:
        return "Science"
print(func(4.2,"zuka"))
    