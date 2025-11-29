from math import ceil
def is_prime(n):
    for i in range(2, ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True