from weapon import Weapon

class Robot:
    def __init__(self, name,health):
        self.name = name
        self.health = health
        self.weapons = [Weapon('Photon cannon',10)]
        #self.create_weapons()
        
        
    def attack(self, dinosaur):
        dinosaur -= self.weapons[0].attack_power
        return dinosaur
    def create_weapons(self):
        self.weapons.append(Weapon('Photon cannon',10))
        self.weapons.append(Weapon('Plasma Gun', 15))
        self.weapons.append(Weapon('minigun', 30))
    
dino = 20
test_robot = Robot('')
dino = test_robot.attack(dino)
print(dino)