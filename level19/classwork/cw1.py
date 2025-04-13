def six_toast(num):
    return abs(num-6)


#2) შექმენით ორი ლისთი და ლუპის მეშევოებით შექმენით ახალი ლისთი რომელიც იქნება ამ ორის გაერთანება

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=[]
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
print(list3)


#3) შექმენით ფუნქცია რომელიც იღებს მასივს და აბრუნებს ახალ მასივს კენტი ელემენტების გარეშე

lstn=[1,2,3,4,5,6,7,8,9,10]
res=[]
if i %2==0:
    res+=i
    return res
    print(res)
