def even(lst):
    evens = [x for x in lst if x % 2 == 0] 
    return evens 

nums = [1, 2, 3, 4, 5, 6]
print(even(nums))
