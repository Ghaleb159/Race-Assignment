import random


class Vehicle:
    def __init__(self, name, HP, Enginesize, Body):
        self.name = name
        self.HP = HP
        self.Enginesize = Enginesize
        self.Body = Body


    def race(self):
        Dice_roll = random.randrange(2,12)
        return self.Body + self.Enginesize + self.HP * Dice_roll
    