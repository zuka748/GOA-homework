def is_square(n):
    if n < 0:
        return False
    k = int(n**0.5)
    return k * k == n
