from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    def create_fleet(self):
        self.robots.append(Robot('Android', 50,50))
        self.robots.append(Robot('T-800', 60,50))
        self.robots.append(Robot('Megatron', 75,50))
    def display_stats(self):
        print('Current Robot Fleet: ')
        for i in range(len(self.robots)):
            print(f'{i}. {self.robots[i].name} ({self.robots[i].health} health, {self.robots[i].power} power)')