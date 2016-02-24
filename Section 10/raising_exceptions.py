# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readfile('xlines.doc'):
            # print the current line, but strip the CR or NL etc from it
            print(line.strip())
    except FileNotFoundError as e:
        print("Can not open file:", e)
        
    except ValueError as e:
        print('Bad Filename structure:', e)
        
def readfile(filename):
    # create our own exception if the filename doesn't end with .txt
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')

if __name__ == "__main__": main()