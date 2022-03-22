import random
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.heard = Herd()
    def run_game(self):
        pass
    def display_welcome(self):
        print('Welcome to Robots Versus Dinosaurs!')
        print('----------')
    def battle(self):
        winner = False
        round = 1
        coin_toss = self.coin_toss()
        if coin_toss == 'Heads':
            print("Heads! The Robots will go first")
        else:
            print('Tails! The Dinosaurs will go first')
        while winner == False:
            print(f'Round {round}')     
            if coin_toss == 'Heads':
                self.robo_turn()
                if len(self.heard.dinosaurs) == 0:
                    winner = True
                self.dino_turn()
                if len(self.fleet.robots) == 0:
                    winner = True
            else:
                self.dino_turn()
                if len(self.fleet.robots) == 0:
                    winner = True
                self.robo_turn()
                if len(self.heard.dinosaurs) == 0:
                    winner = True
            round += 1
        self.display_winners()
        
    def dino_turn(self,):
        self.heard.display_stats()
        attacker = int(input('Select the dinosaur to attack with: '))
        self.fleet.display_stats()
        defender = int(input('Select robot to defend'))
        self.heard.dinosaurs[attacker].attack(self.fleet.robots[defender])
    def robo_turn(self):
        self.fleet.display_stats()
        attacker = int(input('Select the robot to attack with: '))
        self.heard.display_stats()
        defender = int(input('Select dinosaur to defend: '))
        self.fleet.robots[attacker].attack(self.heard.dinosaurs[defender])
    def show_dino_opponet_options(self): #robot stats
        pass
    def show_robo_opponet_options(self): # dino stats
        pass
    def display_winners(self):
        if len(self.heard.dinosaurs) == 0:
            print('The Robots won!')
        elif len(self.fleet.robots) == 0:
            print('The Dinosaurs won!')
    def coin_toss(self):
        return random.choice(['Heads','Tails'])
        

test = Battlefield()
test.battle()