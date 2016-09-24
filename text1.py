class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        #self.name = name
        #print(sounds)
        #print(name)

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)] + " ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Bong", "Tink", "Tik", "Tak", "Hugga Digga Burr"])

    def keep_time(self):
        print("one two three four")

    def ignite(self):
        print("PFCHHHHHKKKKOOOOOOHH i.e. big fire boom sound")
        
class Band(Drummer):
    def __init__(self):
        print("Band created")

    def hire(self):
        print( "you're hired!")

    def fire(self):
        print("you're FIRED!")

def main():
    bonzo = Drummer()
    bonzo.keep_time()
    bonzo.solo(8)
    slash = Guitarist()
    slash.solo(8)
    bonzo.ignite()
    RHCP = Band()
    RHCP.hire()

if __name__ == "__main__":
    main()