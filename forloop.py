# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    # suppressing the default new line after a print via 'end'
    print(line, end='')