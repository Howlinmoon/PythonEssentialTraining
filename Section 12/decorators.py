# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    # an accessor is created via an @ sign
    # reminds me of overloading from Java
    @property
    def color(self):
        return self.properties.get('color', None)

    # now we use that property as a setter
    @color.setter
    def color(self, c):
        self.properties['color'] = c

    # and likewise a deleter
    @color.deleter
    def color(self):
        del self.properties['color']


def main():
    donald = Duck()
    # set donald's color
    donald.color = 'blue'
    print(donald.color)

if __name__ == "__main__": main()
