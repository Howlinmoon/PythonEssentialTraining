# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

    funky(5, 6, 7, 8, 9, 10, scooby = 1, shaggy = 2, velma = 42)

# experimenting with a list of optional arguments
# *args is used for simple lists of args
# **kwargs is used for key/value pairs of args
def testfunc(this, that, other, *args, **kwargs):
    print('This is a test function that was passed the following')
    print("this {}, that {}, other {}".format(this, that, other))
    print("and the following loose arguments: {}".format(args))
    print("followed by the optional named arguments")
    print(kwargs['one'], kwargs['two'], kwargs['four'])
    
# handling kwargs when the keys are not known in advance
def funky(this, that, other, *args, **kwargs):
    for k in kwargs:
        print("kwargs contains key: {} with value: {}".format(k, kwargs[k]))

if __name__ == "__main__":
    main()