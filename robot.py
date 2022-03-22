from weapon import Weapon


class Robot:
    def __init__(self, name,health, power):
        self.name = name
        self.health = health
        self.power = power
        self.weapons = []
        self.create_weapons()
    def attack(self, dinosaur):
        self.display_weapons()
        user_input= int(input('Enter weapon selection: '))
        dinosaur.health -= self.weapons[user_input].attack_power
        self.power -= 10
        print(f'{dinosaur.name} was hit with {self.weapons[user_input].attack_power} damage')
        print('----------')
    def create_weapons(self):
        self.weapons.append(Weapon('Photon cannon',10))
        self.weapons.append(Weapon('Plasma Gun', 20))
        self.weapons.append(Weapon('minigun', 30))
    def display_weapons(self):
        print('Robot Weapons:')
        for i in range(len(self.weapons)):
            print(f'{i}. {self.weapons[i].name} ({self.weapons[i].attack_power} attack power)')