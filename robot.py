from weapon import Weapon


class Robot:
    def __init__(self, name,health):
        self.name = name
        self.health = health
        self.weapons = [Weapon('Photon cannon',10)]
        self.initiative = 0
        #self.create_weapons()
    def attack(self, dinosaur):
        dinosaur.health -= self.weapons[0].attack_power
    def create_weapons(self):
        self.weapons.append(Weapon('Photon cannon',10))
        self.weapons.append(Weapon('Plasma Gun', 15))
        self.weapons.append(Weapon('minigun', 30))
        
