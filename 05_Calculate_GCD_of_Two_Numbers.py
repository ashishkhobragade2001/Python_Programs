def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))
# Output: 6

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))  # Output: 6

n1=12
n2=18
def my_method(n1,n2):
    return max([i for i in range(1,n1+1) if (n1%i==0 and n2%i==0)])
print("greatest common factor is :",my_method(n1,n2))
    
