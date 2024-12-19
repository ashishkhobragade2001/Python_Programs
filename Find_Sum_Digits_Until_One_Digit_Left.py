def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

n = 38
print("Single digit sum:", sum_of_digits(n))
# Output: 2 (3 + 8 = 11, 1 + 1 = 2)
