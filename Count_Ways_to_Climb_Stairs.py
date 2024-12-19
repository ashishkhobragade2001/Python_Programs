def climb_stairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

n = 5
print("Number of ways to climb stairs:", climb_stairs(n))
# Output: 8

def climb(n)
    if n <=2:
        return next
    first,second = 1,2
    for i in range(3,n+1):
        first,second= second,first+second
    return second