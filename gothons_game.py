from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "It hs its sub classes"
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):
    quips =[
        "you died",
        "your mom would be proud",
        "looser",
        "My puppy is better at this"

    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
class CentralCorridor(Scene):
    def enter(self):
        print '''your ship has been invaded by gothon, go to escape pod and
        destroy ship by laser weapon armory'''

        print """Shoot
        Dodge
        Tell a joke"""
        action = raw_input("")

        if action =="Shoot":
            print"you shoot at gothon and finnaly he kills you"
            return 'death'

        elif action == "Dodge":
            print "you dodge like a boxer but gothon kills you"
            return 'death'

        elif action == "Tell a joke":
            print """you tell him a joke and gothon starts laughing
            then you go shoot him and move to armory"""
            return 'laser_weapon_armory'

        else:
            print "Does not compute!"
            return 'central_corridor'
class LaserWeaponArmory(Scene):
    def enter(self):
        print """ypu are inside the LaserWeaponArmory
        need to pick the bomb. it has lock pad which locks
        forever after 10 attempts,try to unlock it
        """
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input()
        guesses = 0

        while guess != code and guesses < 10:
            print "BBZZZEDDD"
            guesses += 1
            guess = raw_input()

        if guess == code:
            print"""The lock opens,
            grab a neutron bomb"""

        else:
            print"""The lockpad locks forever
            and the ship blown up"""
            return 'death'
class TheBridge(Scene):
    def enter(self):
        print """There are 5 gothons surrounding you
        with armour in your hand,
        what you gonna do???"""

        action = raw_input()

        if action == "throw the bomb":
            print "Gothons kill you"
            return 'death'

        elif action == "place the bomb":
            print """slowly place the bomb
            and move to escape pod"""
            return 'escape_pod'

        else:
            print "Does not compute"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "there are 5 pods which one you take"
        good_pod = randint(1,5)
        guess = raw_input()

        if int(guess) != good_pod:
            return 'death'
        else:
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "You won!"
        return 'finished'
class Map(object):
    scenes ={
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

map = Map('central_corridor')
game = Engine(map)
game.play()
