from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    def create_fleet(self):
        self.robots.append(Robot('T-800', 50))
        self.robots.append(Robot('Android', 75))
        self.robots.append(Robot('Megatron', 100))
