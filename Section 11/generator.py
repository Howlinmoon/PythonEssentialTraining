# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(5,25,5):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('Requires at least one argument!')
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))

    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()