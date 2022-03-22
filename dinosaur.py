class Dinosaur:
    def __init__(self, name, health, attack_power, energy):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.energy = energy
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{robot.name} was hit with {self.attack_power} damage')