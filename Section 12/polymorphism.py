# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


class Dog:
    def bark(self):
        print("Woof Woof!")

    def fur(self):
        print("The dog has brown and white fur")

    def walk(self):
        print("Walks like a dog")

    def quack(self):
        print("The dog can not quack")


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print("The duck can not bark")

    def fur(self):
        print("The duck has feathers")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.bark()
    fido.fur()

    for o in (donald, fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == "__main__": main()