# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        print("The constructor has been called")
        # assume the color assignment is being made via
        # the key 'color'
        # we access the key 'color' if it exists, otherwise
        # we default to using 'white'
        # self._color = kwargs.get('color', 'white')

        # save our properties in a dictionary
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # get the color the proper way
    def get_variable(self, k):
        return self.variables.get(k, None)

    # set the color the proper way
    def set_variable(self, k, v):
        self.variables[k] = v

def main():
    donald = Duck(color='organge')
    # accessing a property externally - bad practice!
    # print(donald._color)
    # override the property externally - bad practice!
    # donald._color = 'green'

    # accessing a property externally - bad practice!
    # print(donald._color)

    # changing the color the proper way
    # donald.set_color("Red")
    # retrieving the color the proper way
    print(donald.get_variable('color'))
    donald.quack()
    donald.walk()

    donald.set_variable('feet', 3)
    print("Donald has {} feet".format(donald.get_variable('feet')))

if __name__ == "__main__": main()