from sys import exit

def start():
    print "You're in a dark room"
    print "There is a door to your left and right"
    print "Choose left or right"

    #enter left or right
    choice = raw_input()

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You starve")

def bear_room():
    #A bear in front of the door.
    #take honey
    #or move the bear_room

    bear_moved = False
    while True:

        print "Choose take honey,open door or taunt bear_room to move the bear away "
        choice = raw_input()
        if choice == "take honey":
            dead("Bear slaps you and you're dead")
        elif choice == "taunt bear" and not bear_moved:
            print "Bear has moved"
            bear_moved = True
        elif choice == "taunr bear" and bear_moved:
            dead("Bear kills you")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "No idea"

def gold_room():
    print "Room full of gold"

    choice = raw_input()
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, type a number")

    if how_much < 50:
        print "You win"
        exit(0)
    else:
        dead("You're greedy")

def cthulhu_room():
    print "Devil cthulhu"

    print "flee or head"
    choice = raw_input()

    if choice == "flee":
        start()
    elif choice == "head":
        dead("Eats your head")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

start()
