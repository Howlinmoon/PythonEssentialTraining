# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, value):
        print("The constructor has been called")
        # self._numQuacks is bound to the object - not the class
        self._numQuacks = value

    def quack(self):
        print('Quaaack!' * self._numQuacks)

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck(13)

    donald.quack()
    donald.walk()

    daisy = Duck(20)
    daisy.quack()

if __name__ == "__main__": main()