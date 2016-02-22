# utility function
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# generator function
# using 'yield' instead of return allows the function to temporarily end
# and then resume at the same spot later.
def primes(n = 1):
    while(True):
        if isprime(n):
            yield n
        n += 1 

for n in primes():
    print(n)
    if n > 100: break
