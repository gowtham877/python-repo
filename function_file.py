from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line, f):
    print line, f.readline()

current = open(input_file)
print_all(current)

rewind(current)

line=1
print_line(line,current)
