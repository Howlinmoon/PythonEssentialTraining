# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(20)
    testfunc(112, onemore = 99)
    testfunc(42, onemore=27, another = 13)

# function with one mandatory and two optional parameters
def testfunc(number, another = 47, onemore = 75):
    print('This is a test function', number, another, onemore)

if __name__ == "__main__":
    main()