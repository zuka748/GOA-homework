#შექმენით ფუნქცია რომელიც დაუმატებს ერთმანეთს string-ებს რომელიც გადმოეცემა არგუმენტად, გაითვალისწინეთ რომ თუ რომელიმე არგუმენტი იქნება ineger ის უნდა მოათავსოთ შედგენილი ქინადადების ბოლოშო.

def func(str1, str2):
    if type(str1)==str and type(str2)==str:
        return str1+str2
    elif type(str1)==int or type(str2)==int:
        return str(str1)+str(str2)
print(func(2,"hello"))