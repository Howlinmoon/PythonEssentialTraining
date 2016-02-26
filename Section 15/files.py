# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # defaults to opening file in 'r'ead mode
    f = open('lines.txt')
    for line in f.readlines():
        print(line, end = '')

if __name__ == "__main__": main()