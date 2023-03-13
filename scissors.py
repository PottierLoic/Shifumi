import random
from constants import *

class Scissors:
    def __init__(self, x, y) -> None:
        self.type = "scissors"
        if x == None or y == None:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = x
            self.y = y