# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # a simple regular expression that prints out any line that
        # contains 'Lenore' or 'Nevermore'
        match =  re.search('(Len|Neverm)ore', line)
        if match:
            # print out the word we matched
            print(match.group())
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')

if __name__ == "__main__": main()