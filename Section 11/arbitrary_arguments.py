# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

# experimenting with a list of optional arguments
# that follow manadatory ones
def testfunc(this, that, other, *args):
    print('This is a test function that was passed the following')
    print(this, that, other)
    for n in args:
        print("from args: {}".format(n))

if __name__ == "__main__":
    main()