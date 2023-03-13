from constants import *
from paper import Paper
from rock import Rock
from scissors import Scissors
from quadtree.qtree import QuadTree
from quadtree.rect import Rect



class Game:

    def __init__(self, amount) -> None:
        self.papers = []
        self.scissors = []
        self.rocks = []
        self.quadtree = QuadTree(Rect(0, 0, WIDTH, HEIGHT), CAPACITY)


        for i in range(amount):
            self.papers.append(Paper(None, None))
            self.scissors.append(Scissors(None, None))
            self.rocks.append(Rock(None, None))

    def update(self):
        self.quadtree = QuadTree(Rect(0, 0, WIDTH, HEIGHT), CAPACITY)
        nearby = []
        for paper in self.papers:
            self.quadtree.insert(paper)
        for rock in self.rocks:
            self.quadtree.insert(rock)
        for scissor in self.scissors:
            self.quadtree.insert(scissor)
        
        for paper in self.papers:
            nearby = self.quadtree.query(Rect(0, 0, WIDTH, HEIGHT), nearby)
            for other in nearby:
                if other != paper:
                    if paper.x - other.x < SIZE and paper.y - other.y < SIZE:
                        if other.type == "rock":
                            self.papers.append(Paper(other.x, other.y))
                            self.rocks.remove(other)
        for paper in self.papers:
            for scissors in self.scissors:
                if scissors.x - other.x < SIZE and scissors.y - other.y < SIZE:
                    if other.type == "paper":
                        self.scissors.append(Scissors(other.x, other.y))
                        self.papers.remove(other)
        for rock in self.rocks:
            nearby = self.quadtree.query(Rect(0, 0, WIDTH, HEIGHT), nearby)
            for other in nearby:
                if other != rock:
                    if rock.x - other.x < SIZE and rock.y - other.y < SIZE:
                        if other.type == "scissors":
                            self.rocks.append(Rock(other.x, other.y))
                            self.scissors.remove(other)
