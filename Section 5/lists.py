# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # a tuple
    x = (1, 2, 3)
    print(type(x), x)
    
    # a list
    x = [1, 2, 3]
    print(type(x), x)
    print(id(x), x)
    # add something
    x.append(5)
    # print it out again - notice the id does not change
    print(id(x), x)
    
    # back to strings
    x = "this is a string"
    print(type(x), x)
    
    print("a slice of the string: {}".format(x[3:7]))
    
    x = (1, 2, 3, 56, 121, 99, 1901)
    for i in x:
        print(i, end = " ")
    print()
    
    
    
if __name__ == "__main__": main()