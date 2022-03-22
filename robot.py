from weapon import Weapon


class Robot:
    def __init__(self, name,health, power):
        self.name = name
        self.health = health
        self.power = power
        self.weapons = []
        self.create_weapons()
    def attack(self, dinosaur):
        print('----------')
        dinosaur.health -= self.weapons[0].attack_power
        print(f'{dinosaur.name} was hit with {self.weapons[0].attack_power} damage')
    def create_weapons(self):
        self.weapons.append(Weapon('Photon cannon',10))
        self.weapons.append(Weapon('Plasma Gun', 15))
        self.weapons.append(Weapon('minigun', 30))
        
