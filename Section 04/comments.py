# comments.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in primes():
        # create a list of prime numbers less than 100
        if n > 100: break
        print(n)

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            # found a divisor, not prime
            return False
    else:
        return True

def primes(n = 1):
    # note, we start with a default of 1...
    while(True):
        # yield makes this a generator function
        if isprime(n): yield n
        n += 1 

if __name__ == "__main__": main()