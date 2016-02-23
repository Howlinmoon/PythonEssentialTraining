# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    # for efficiency, we are going to pre-compile the static regex instead of dynamically instantiating it for every line
    # we will make this pattern case insensitive with the re.IGNORECASE switch
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        # a simple regular expression that prints out any line that
        # contains 'Lenore' or 'Nevermore'
        if re.search(pattern, line):
            print(pattern.sub('chicken', line), end='')

if __name__ == "__main__": main()