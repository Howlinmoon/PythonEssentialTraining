# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk(self):
        print("I have something to say")

    def walk(self):
        print("Hey, I'm walkin' here!")

    def clothes(self):
        print("I have spiffy clothes")

# making 'Duck' inherit from 'Animal'
class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        # now, use the super method from our parent class
        super().walk()

# Dog can inherit from Animal also
class Dog(Animal):
    # and provide it's own clothes method
    def clothes(self):
        print("I have brown and white fur, thank you very much!")

def main():
    donald = Duck()

    donald.quack()
    donald.walk()
    donald.talk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()