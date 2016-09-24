#Create Musician class
#Define shortcut w __init__ to make sure instances contain sound attributE

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end= " ") #used to make sure no error message since we call for 6 len, but only have 3 sounds
        print()    
        
class Bassist(Musician): #Musician is parent of Bassist
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])
        
class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Blam", "Thrumb", "Zing"])

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")

    def count(self):
        for n in range(1,5):
            print(n)
    
    def combust(self):
        print("BOOM!")
        
class Band(object):
    def hire(self):
        print("You're hired!")
    def fire(self):
        print("You're fired!")

def set():
    Charlie = Drummer()
    Charlie.count()
    Charlie.solo(8)
    Keith = Guitarist()
    Keith.solo(8)
    Ronnie = Bassist()
    Ronnie.solo(8)
    Charlie.combust()
    Stones = Band()
    Stones.fire()

if __name__ == "__main__":
    set()

        