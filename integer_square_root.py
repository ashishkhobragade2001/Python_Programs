def integer_square_root(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0:
        return 0

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid + 1
        else:
            right = mid
    return left - 1

n = 16
print("Integer square root:", integer_square_root(n))
# Output: 4
