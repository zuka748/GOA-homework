def unique_numbers(lst):
    result = []
    for i in lst:
        if lst.count(i) == 1:   
            result.append(i)    
    return result

nums = [1, 2, 2, 3, 4, 4, 5]
print(unique_numbers(nums))  
