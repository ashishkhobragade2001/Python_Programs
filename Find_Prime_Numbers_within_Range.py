def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print("Primes between 10 and 50:", primes_in_range(10, 50))
# Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
