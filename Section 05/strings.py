# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = "this is a\n string!"
    # evaluates the escape character
    print(s)
    
    # raw strings - used mainly with regular expressions
    s = r"ignores the escape \n character"
    print(s)

    n = 42
    s = "this string contains the number {} see it is there!".format(n)
    print(s)
    
    multiLineString = ''' This is a multi-line
    String that is spanning
    three lines'''
    
    print(multiLineString)
if __name__ == "__main__": main()