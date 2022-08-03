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

#Array of tanks
tanks = []
for i in range(0,5,1):
    name = "Tank %i" % i 
    tanks.append(Tank(name))

round = 1
while len(tanks)>1 :
    #Select the attaking tank
    tankAttacking = tanks[random.randrange(0,len(tanks))]
    tankHitted = tankAttacking

    #Select the defending tank
    while tankAttacking == tankHitted:
        tankHitted = tanks[random.randrange(0,len(tanks))]
    
    #Attack
    print("Round %i" % round)
    tankAttacking.fire_at(tankHitted)

    #Check if the deffending tank is dead and remove it from game
    if not tankHitted.alive:
        tanks.remove(tankHitted)

    round += 1
    print()

#Show the tank winner
print("The winner is: %s" % tanks[0]) 