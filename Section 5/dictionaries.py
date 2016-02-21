# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = { 'one':1, 'two':2, 'three':3, 'four':4, 'five':5 }
    print(d)
    # normal randomish order
    for k in d:
        print(k, d[k])

    print("Sorted order by key name")
    for k in sorted(d.keys()):
        print(k, d[k])

    # another style of dictionary definition
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    
    # adhoc add a key/value
    d['seven'] = 7
    
    print("Second style sorted order by key name")
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()
