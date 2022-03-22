from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    def create_herd(self):
        self.dinosaurs.append(Dinosaur('Velociraptor', 50, 50,))
        self.dinosaurs.append(Dinosaur('Stegosaurus', 60, 50,))
        self.dinosaurs.append(Dinosaur('T-rex', 75, 50,))
    def display_stats(self):
        print('Current Dinosaur Herd:')
        for i in range(len(self.dinosaurs)):
            print(f'{i}. {self.dinosaurs[i].name} ({self.dinosaurs[i].health} health, {self.dinosaurs[i].energy} energy)')