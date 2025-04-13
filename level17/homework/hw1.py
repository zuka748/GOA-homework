# 1. შექმენით manual_remove ფუნქცია
# def manual_remove(lst):
#     res=[]
#     for i in lst:
#         if i not in res:
#             res.append(i)
#     return res        
# print(manual_remove([1,2,3,4,5]))


# 2. შექმენით manual_index ფუნქია

# def manual_index(l,x):
#     for i in range(len(l)):
#         if l[i]==x:
#             return i
        

# 3. შექმენით manual_len ფუნქცია

def manual_len(lst1):
    count=0
    for i in lst1:
        
            count+=1
    return count
print(manual_len([1,2,3,4,5]))

# 4. შექმენით manual_pop ფუნქცია

def manual_pop(lst2):
    return lst2 [:-1]
print(manual_pop([1,2,3,4,5]))


# 5. შექმენით manual_reverse ფუნქცია

def manual_reverse(l):
     return l [::-1]
print(manual_reverse([1,2,3,4,5]))
    