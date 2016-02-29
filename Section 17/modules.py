# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print('System Platform: {}'.format(sys.platform))

    import os
    print('OS Name: {}'.format(os.name))
    print('Current Path: {}'.format(os.getenv('PATH')))
    print('Current Working Directory: {}'.format(os.getcwd()))

    #import urllib.request
    #page = urllib.request.urlopen('http://www.bw.org')
    #for line in page:
    #    print(str(line, encoding='utf_8'), end = '')

    import random
    print(random.randint(1, 1000))

    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)


    import datetime
    now = datetime.datetime.now()
    print("The time is now: {}".format(now))
    print(now.year, now.month, now.day, now.hour, now.minute)

if __name__ == "__main__": main()