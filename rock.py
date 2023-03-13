import random
from constants import *

class Rock:
    def __init__(self, x, y) -> None:
        self.type = "rock"
        if x == None or y == None:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = x
            self.y = y