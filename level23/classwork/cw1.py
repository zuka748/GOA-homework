# 1. შემოატანინეთ მომხმარებელს თავისი ასაკი და შეამოწმეთ, თუ ის 10-წლისაა ან უფრო პატარა, დაპრინტეთ "Kid", თუ 10-ზე მეტი და 18-ზე ნაკლები გამოიტანეთ "teenager", თუ 18-ზე მეტია და 30-ზე ნაკლები "adult", სხვა შემთხვევაში "unc"

age=int(input("asaki"))
if age <=10:
    print("kid", end="")
elif age > 10 and age <18:
    print("teenager",end="")
elif age >=18 and age < 30:
    print("adult", end="")
else:
    print("adult", end="")

#2
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count_positives = 0
    sum_negatives = 0

    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num

    return [count_positives, sum_negatives]

#3
def is_opposite(s1, s2):
    if not s1 or not s2:
        return False
    return s1.swapcase() == s2

#4
def monkey_count(n):
    return list(range(1, n + 1))
