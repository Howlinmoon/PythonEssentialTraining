# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


# an experimental class
class Egg:
    # create our constructor
    def __init__(self, kind = "fried"):
        self.kind = kind
    
    def whatKind(self):
        return self.kind

def main():
    friedEggs = Egg()
    scrambledEggs = Egg("scrambled")
    print("friedEggs is kind: {}".format(friedEggs.whatKind()))
    print("scrambledEggs is kind: {}".format(scrambledEggs.whatKind()))
    
    
if __name__ == "__main__": main()