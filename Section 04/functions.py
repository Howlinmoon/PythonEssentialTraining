# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# main is a function - takes no parameters
def main():
    func()
    func()
    func()

# a counting function
def func():
    for i in range(10):
        print(i, end = ' ')
    print()

if __name__ == "__main__": main()
