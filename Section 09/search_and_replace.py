# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # a simple regular expression that matches any line that
        # contains 'Lenore' or 'Nevermore'
        # and replaces the matched test with 'newText'
        print(re.sub('(Len|Neverm)ore', 'newText', line), end='')
        # 'sub' performs the search and replace all in a single operation
        
        # breaking it down into a search and replace:
        match = re.search('(Len|Neverm)ore', line)
        # did we find a match?
        if match:
            print(line.replace(match.group(), 'matchText'), end='')

if __name__ == "__main__": main()