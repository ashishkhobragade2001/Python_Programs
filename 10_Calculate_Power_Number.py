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

n=3
p=2
def my_method(n,p):
    return n**p
print("power is :",my_method(n,p))

a = 1
def my_method_02(n,p):
    global a
    a = 1
    for i in range(p):
        a *= n
    return a
    
print("mera power :",my_method_02(n,p))