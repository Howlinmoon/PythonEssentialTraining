# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 3, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

    # conditional expressions
    s = "Less than" if a < b else "Not less than"
    print(s)

if __name__ == "__main__": main()
