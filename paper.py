import random
from constants import *

class Paper:
    def __init__(self, x, y) -> None:
        self.type = "paper"
        if x == None or y == None:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = x
            self.y = y