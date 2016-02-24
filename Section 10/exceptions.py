# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('xlines.txt')
    except FileNotFoundError as e:
        print("Could not open the file, try again tomorrow...")
        print(e)
    else:
        for line in fh:
            # print the current line, but strip the CR or NL etc from it
            print(line.strip())

if __name__ == "__main__": main()