from attack_style import Attack_style
class Dinosaur:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy
        self.attacks = []
        self.create_attacks()
    def attack(self, robot):
        self.display_attacks()
        user_input = int(input('Enter Atack style: '))
        robot.health -= self.attacks[user_input].attack_power
        print(f'{robot.name} was hit with {self.attacks[user_input].attack_power} damage')
        print('----------')
    def create_attacks(self):
        self.attacks.append(Attack_style('Tail Whip', 10))
        self.attacks.append(Attack_style('Bite', 20))
        self.attacks.append(Attack_style('Chomp', 30))
    def display_attacks(self):
        print('Dinosaurs Attack Styles:')
        for i in range(len(self.attacks)):
            print(f'{i}. {self.attacks[i].name} ({self.attacks[i].attack_power} attack power)')