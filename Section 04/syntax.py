# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the syntax.py file.")
    egg()
print("This is line is printed first")

def egg():
    print("egg was called")

# only run the following code (the call to main() ) if this is the primary executable file
# if this file is sourced by some other file, main() will not get called.
if __name__ == "__main__":
    main()