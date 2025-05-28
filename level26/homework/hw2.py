# 3. შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს ლისტს და გამოიტანეთ ის data type რომელიც ყველაზე ხშირად გვხვდება ამ ლისტსში.

def lstn(lst1):
    ints=0
    strs=0
    floats=0
    for i in lst1:
        if type(i)==int:
            ints+=1
        elif type(i)==str:
            strs+=1
        elif type(i)==float:
            floats+=1

    if ints>strs and ints>floats:
        return int
    elif strs>ints and strs>floats:
        return str
    else:
        return float

        
