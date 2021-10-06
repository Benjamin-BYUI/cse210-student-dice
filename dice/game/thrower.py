import random

class Thrower:
    """A code template for a person who plays the game. The responsibility of 
    this class of objects is to roll the dice, count up the points score of 
    that round, and determine if another throw is allowed.
    
    Attributes:
        dice (list): The dice values in list form.
        num_throws (number): The total number of throws so far.
        round_points (number): The current round dice score.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of Thrower.
        """
        self.dice = []
        self.num_throws = 0
        self.round_points = 0
        
    def throw_dice(self):
        """generates a list of dice values into the class attribute dice. Increments
        throw number attribute.
        
        Args:
            self (Throwe): an instance of Director.
        """
        self.dice = []
        for i in range (6):
            die = random.randint(1, 6)
            self.dice.append(die)
        self.num_throws += 1

    def get_points(self):
        """Calculates points from current dice roll.
        
        Args:
            self (Director): an instance of Director.
        Returns:
            Score of current dice roll.
        """
        self.round_points = 0
        for die in self.dice:
            if die == 1:
                self.round_points += 100
            elif die == 5:
                self.round_points += 50
        return self.round_points
        
    def can_throw(self):
        """Determines if another throw is valid.
        
        Args:
            self (Director): an instance of Director.
        Returns: False if the current dice score is 0, otherwise true.

        """
        if self.round_points == 0:
            return False
        return True
