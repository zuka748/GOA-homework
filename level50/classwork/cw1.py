#1
def square_digits(num):
    result = ""
    for digit in str(num):
        squared = int(digit) ** 2
        result += str(squared)
    return int(result)

#2
def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]