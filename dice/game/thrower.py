import random

class Thrower:

    def __init__(self):
        self.dice = []
        self.num_throws = 0
        self.round_points = 0
        
    def throw_dice(self):
        self.dice = []
        for i in range (6):
            die = random.randint(1, 6)
            self.dice.append(die)
        self.num_throws += 1

    def get_points(self):
        self.round_points = 0
        for die in self.dice:
            if die == 1:
                self.round_points += 100
            elif die == 5:
                self.round_points += 50
        return self.round_points
        
    def can_throw(self):
        if self.round_points == 0:
            return False
        return True
