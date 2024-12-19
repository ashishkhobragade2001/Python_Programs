def largest_prime_factor(number):
    def is_prime(num):
        return all([i for i in range(2,num) if num%i !=0])
    primes = []
    for i in range(2,number):
        if is_prime(i):
            primes.append(i)
        
    prime_factor = []
    for i in primes:
        if number % i == 0:
            prime_factor.append(i)
           
    return max(prime_factor)
print(largest_prime_factor(51))
    