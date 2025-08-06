def unique_sum(lst):
    if not lst:
        return None
    
    sum1 = []
    total = 0
    
    for num in lst:
        if num not in sum1:
            sum1.append(num)
            total += num
    
    return total