from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    def create_herd(self):
        self.dinosaurs.append(Dinosaur('Velociraptor', 50, 10))
        self.dinosaurs.append(Dinosaur('Stegosaurus', 75, 15))
        self.dinosaurs.append(Dinosaur('T-rex', 100, 20))
   