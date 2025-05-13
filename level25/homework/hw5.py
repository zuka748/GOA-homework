def digitize(n):
    strn=str(n)
    res=[]
    for i in strn:
        res.append(int(i))
    return res[::-1]
print(digitize(1,2,3))