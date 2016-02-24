# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a sad little string'
    for c in s:
        # skip printing of any 's' characters
        if c == 's':
            continue
        # stop when we encounter an 'e'
        if c == 'e':
            break
        print(c, end='')
        
    print()

    for c in s:
        print(c, end='')
    else:
        print("\nThe for loop has ended, thus I am printed")
    print("Not sure why its simply not printed above me...")

if __name__ == "__main__": main()