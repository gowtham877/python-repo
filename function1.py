def print1(*args):
    arg1, arg2 = args
    print "arg1:%r, arg2:%r" % (arg1,arg2)

def print2(arg1, arg2):
    print "arg1:%r,arg2:%r" % (arg1,arg2)

print1("Hello","there!")
print2("stay","home")
