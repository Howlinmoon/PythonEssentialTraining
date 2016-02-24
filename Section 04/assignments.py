# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a = "one"
    print(type(a), a)
    # assigning multiple values at once
    x, y = 99, "hello"
    print(x,y)
    # a simple swap
    x, y = y, x
    print(x,y)

if __name__ == "__main__": main()
