print "ENter room no.1 or room no.2 ?"

door = raw_input("")

if door == "1":
    print "Room no.1"
    bear = raw_input()

    if bear == "1":
        print "Bear 1"

    elif bear == "2":
        print "Bear 2"

    else:
        print "No bear"

elif door == "2":
    print "Room no.2"
    deer = raw_input()

    if deer == "1":
        print "Deer 1"

    elif deer == "2":
        print "Deer 2"

    else:
        print "no deer"

else:
    print "Select a valid door"
