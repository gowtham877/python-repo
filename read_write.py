from sys import argv

script, filename = argv

print "erasing %r" % filename
#input("?")

print "Opening the file..."
target = open(filename, 'w')

target.truncate()

line1=raw_input("line1: ")
line2=raw_input("line2: ")
line3=raw_input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
