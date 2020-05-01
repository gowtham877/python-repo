str1 = "Hey there how are you wassup"

str2 = str1.split(' ')
print str2

list1 = ["Im", "doing", "great"]
print list1

while len(str2) != 10:
    print "hello"
    next = list1.pop()
    str2.append(next)

print str2

print str2[1]

print str2.pop()
print ' '.join(str2)
print ' '.join(str2[])
