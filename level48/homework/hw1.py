numbers=[1,2,3,1,4,5,3,2,7]
duplicates=[]

for num in numbers:
    if numbers.count(num) >1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)