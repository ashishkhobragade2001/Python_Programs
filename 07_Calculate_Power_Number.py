def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

x, n = 2, 10
print("Power:", power(x, n))
# Output: 1024
