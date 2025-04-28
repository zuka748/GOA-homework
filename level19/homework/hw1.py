## 1. შექმენით ფუნქცია, რომელიც აერთებს ორ ლისტს (ორივეში მხოლოდ integer-ებია) და ასევე ალაგებს მათ ზრდადობის მიხედვით.

lst1=[1,2,8,4,5]
lst2=[6,7,3,9]
res=lst1+lst2
res.sort()
print(res)

#2

def bigger_sum_in(list1,list2):
    n1=sum(10,20,30,90)
    n2=sum(20,30,40)
    if n1>n2:
        print(n1)
    else:
        print(n2)


# 3. შექმენით ფუნქცია რომელიც იღებ არგუმენტებად ორ ლისტს და აბრუნებს დადებითი რიცხვების რაოდენობასა და უარყოფითების ჯამს (ცალ-ცალკე).

def count_positives_sum_negatives(lst1, lst2):
    all_numbers = lst1 + lst2
    positives = 0
    negatives_sum = 0
    for i in all_numbers:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives_sum += i
    return positives, negatives_sum


# 4. შექმენით ფუნქცია რომელიც არგუმენტად იღებს ლისტს და შლის ყველა ელემენტს რომელიც უნაშთოდ იყოფა 3-ზე


lstn=[1,30,9,6,5,4,7,8]
res=[]
for i in lstn:
    if i % 3!=0:
        res.append (i)
print(res)
        


# 5. შექმენით ფუნქცია რომელსაც გამოაქვს არგუმენტად გადაცემული ლისტის ფორმა, სადაც ყველა ელემენტი გარომაგებულია 2-ზე, მაგალითად input: [2,3,4,5], output: [4,6,8,10]


lst7=[20,40,50,100]
res=[]
for i in lst7:
    res.append(i*2)
    print(res)