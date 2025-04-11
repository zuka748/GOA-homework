#```შექმენით ფუნქცია, რომელსაც გადაეცემა შემდეგი ლისთი: [1,23,165,2,3,92,10,34,911] და ერთი ინტეჯერი(მაგ. 3), თქვენი დავალებაა, რომ ახალ ცარიელ ლისთში შეინხოთ მხოლოდ ისეთი რიცხვები, რომლებიც უნაშთოთ იყოფიან გადმოცემულ ინტეჯერზე(ამ შემთხვევაში 3-ზე).```

#nums=[1,23,165,2,3,92,10,34,911]
#res=[]
#for i in nums:
#   if i % 3==0:
#        res.append(i)
#print(res)


#1
def flt(Z,num):
    res=[]
    for i in Z:
        if i % num == 0:
            res.append(i)
    return res
print(flt([1,23,165,2,3,92,10,34,911],3)) 


#2
def reverse_list(l):
    return l[::-1]

#3

def even_last(numbers): 
    if numbers ==[]:
        return 0
    sum=0
    for i in range(0, len(numbers), 2 ):
        sum+=numbers[i]
    return sum * numbers [-1]