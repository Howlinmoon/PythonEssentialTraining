def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        print("n = {}, x = {}".format(n,x))
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False

    # if it fails all of the non-prime checks, it must be a prime
    print(n, "is a prime number")
    return True

# call the function in a loop
for n in range(1, 24):
    isprime(n)
