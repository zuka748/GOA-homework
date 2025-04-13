#1
def manual_sum(l):
    res=0
    for i in l:
        res +=i
    return res
result=manual_sum([1,2,3,4,5])
print(result)


#2

def manual_append(l,x):
    l.insert(-1,x)
    return l
print (manual_append(list, "z"))