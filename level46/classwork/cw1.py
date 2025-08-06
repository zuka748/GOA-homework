def sum_two_smallest_numbers(numbers):
    numbers.sort()  
    return numbers[0] + numbers[1] 

#2
def get_min_max(seq):
    return (min(seq), max(seq))