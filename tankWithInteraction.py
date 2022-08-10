import random

#Create a class named Tank
class Tank(object):
    #Create the constructor
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    #Create the "toString" method
    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name
    
    #Create a method to fire in another tank, it this one has shells
    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy)
            enemy.hit()
        else:
            print(self.name, "has no shells!")
    
    #Create a method to be executed when the tank is hitted
    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    #Create a method to be executed when the tank has no more armor
    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

tanks = {} #Array of tanks
keys = tanks.keys() #Tanks keys
round = 1

#Start the game
print("TANK WAR")

while True:
    numberOfTanks = int(input("Inform the number of player (2~10): "))
    if numberOfTanks >=2 and numberOfTanks <= 10 :
        break
    else:
        print("Please, select a number between 2 and 10")

#Create so many tanks as requested
#Use chr to define keys from A to J
for i in range(65,(65 + numberOfTanks),1):
    name = input("Define the name of Player %s: " % chr(i))
    tanks[chr(i)] = Tank(name)

while len(tanks)>1 :
    listOfKeys = list(keys)
    #Select the attaking tank
    print("Round %i" % round)
    while len(listOfKeys) > 0 :
        tankAttackingKey = random.choice(listOfKeys)
        tankAttacking = tanks.get(tankAttackingKey)

        print()
        #Select the defending tank
        print("The player %s will attack" % tankAttacking.name)
        while True:
            print()
            tankHittedKey = input("What player you will attack? (A~%s)" % chr(64+len(tanks))).upper()
            if list(keys).count(tankHittedKey) :
                tankHitted = tanks.get(tankHittedKey)
                if not tankHitted == tankAttacking:
                    break
                else:
                    print("You can't attack yourself! :/")
            else :
                print("%s is not an alive/valid player! Select another" % tankHittedKey)
        
        #Attack
        tankAttacking.fire_at(tanks.get(tankHittedKey))
        print()

        #Check if the deffending tank is dead and remove it from game
        if not tankHitted.alive:
            tanks.pop(tankHittedKey)
            if listOfKeys.count(tankHittedKey) > 0:
                listOfKeys.remove(tankHittedKey)

        if listOfKeys.count(tankAttackingKey) > 0:
            listOfKeys.remove(tankAttackingKey)

    print("Players:")
    for tank in tanks:
        print("%s: {" % tank)
        print(" %s \n}" % tanks.get(tank))
    
    round += 1
    print()

#Show the tank winner
print("The winner is: %s" % tanks.get(list(keys)[0])) 