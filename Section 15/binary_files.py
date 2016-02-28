# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # have to use buffered io binary files
    # normally, with text files you can use line oriented operations
    buffersize = 50000
    # 'rb' in binary, 'wb' = write in binary
    infile = open('olives.jpg', 'rb')
    outfile = open("newbin.jpg", "wb")
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done')

if __name__ == "__main__": main()