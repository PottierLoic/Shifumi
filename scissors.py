import random
from constants import *

class Scissors:
    def __init__(self, x, y) -> None:
        self.type = "scissors"
        if x == None or y == None:
            self.x = random.randint(SIZE/2, WIDTH-SIZE/2)
            self.y = random.randint(SIZE/2, HEIGHT-SIZE/2)
        else:
            self.x = x
            self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5