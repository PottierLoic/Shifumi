from constants import *
from paper import Paper
from rock import Rock
from scissors import Scissors
from quadtree.qtree import QuadTree
from quadtree.rect import Rect
import random

class Game:

    def __init__(self, amount) -> None:
        self.papers = []
        self.scissors = []
        self.rocks = []
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)

        for i in range(amount):
            self.papers.append(Paper(None, None))
            self.scissors.append(Scissors(None, None))
            self.rocks.append(Rock(None, None))

    def update(self):
        # destruction/creation part
        # paper / scissors collision part
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for scissors in self.scissors:
            self.quadtree.insert(scissors)
        for paper in self.papers:
            nearby = []
            self.quadtree.query(Rect(paper.x, paper.y, SIZE, SIZE), nearby)
            for other in nearby:
                if abs(paper.x - other.x) < SIZE and abs(paper.y - other.y) < SIZE:
                    self.scissors.append(Scissors(paper.x, paper.y))
                    try:
                        self.papers.remove(paper)
                    except:
                        pass
                    break

        # rock / scissors collision part
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for rock in self.rocks:
            self.quadtree.insert(rock)
        for scissors in self.scissors:
            nearby = []
            self.quadtree.query(Rect(scissors.x, scissors.y, SIZE, SIZE), nearby)
            for other in nearby:
                if abs(scissors.x - other.x) < SIZE and abs(scissors.y - other.y) < SIZE:
                    self.rocks.append(Rock(scissors.x, scissors.y))
                    try:
                        self.scissors.remove(scissors)
                    except:
                        pass
                    break

        # rock / paper collision part
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for paper in self.papers:
            self.quadtree.insert(paper)
        for rock in self.rocks:
            nearby = []
            self.quadtree.query(Rect(rock.x, rock.y, SIZE, SIZE), nearby)
            for other in nearby:
                if abs(rock.x - other.x) < SIZE and abs(rock.y - other.y) < SIZE:
                    self.papers.append(Paper(rock.x, rock.y))
                    try:
                        self.rocks.remove(rock)
                    except:
                        pass
                    break

        # Movement part
        # scissors movements
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for paper in self.papers:
            self.quadtree.insert(paper)
        for scissor in self.scissors:
            nearby = []
            self.quadtree.query(Rect(scissor.x, scissor.y, 100, 100), nearby)
            closest = None
            for paper in nearby:
                if closest is None:
                    closest = paper
                else:
                    if scissor.distance(paper) < scissor.distance(closest):
                        closest = paper
            if closest is not None:
                distx = abs(closest.x - scissor.x)
                disty = abs(closest.y - scissor.y)
                if scissor.x < closest.x:
                    scissor.x += 0.1 * distx/(distx+disty) * SPEED
                elif scissor.x > closest.x:
                    scissor.x -= 0.1 * distx/(distx+disty) * SPEED
                if scissor.y < closest.y:
                    scissor.y += 0.1 * disty/(distx+disty) * SPEED
                elif scissor.y > closest.y:
                    scissor.y -= 0.1 * disty/(distx+disty) * SPEED
            else:
                scissor.x += 0.1 * random.randint(-1, 1) * SPEED
                scissor.y += 0.1 * random.randint(-1, 1) * SPEED

        # paper movements
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for rock in self.rocks:
            self.quadtree.insert(rock)
        for paper in self.papers:
            nearby = []
            self.quadtree.query(Rect(paper.x, paper.y, 100, 100), nearby)
            closest = None
            for rock in nearby:
                if closest is None:
                    closest = rock
                else:
                    if paper.distance(rock) < paper.distance(closest):
                        closest = rock
            if closest is not None:
                distx = abs(closest.x - paper.x)
                disty = abs(closest.y - paper.y)
                if paper.x < closest.x:
                    paper.x += 0.1 * distx/(distx+disty) * SPEED
                elif paper.x > closest.x:
                    paper.x -= 0.1 * distx/(distx+disty) * SPEED
                if paper.y < closest.y:
                    paper.y += 0.1 * disty/(distx+disty) * SPEED
                elif paper.y > closest.y:
                    paper.y -= 0.1 * disty/(distx+disty) * SPEED
            else:
                paper.x += 0.1 * random.randint(-1, 1) * SPEED
                paper.y += 0.1 * random.randint(-1, 1) * SPEED

        # rock movements
        self.quadtree = QuadTree(Rect(WIDTH/2, HEIGHT/2, WIDTH/2, HEIGHT/2), CAPACITY)
        for scissor in self.scissors:
            self.quadtree.insert(scissor)
        for rock in self.rocks:
            nearby = []
            self.quadtree.query(Rect(rock.x, rock.y, 100, 100), nearby)
            closest = None
            for scissor in nearby:
                if closest is None:
                    closest = scissor
                else:
                    if rock.distance(scissor) < rock.distance(closest):
                        closest = scissor
            if closest is not None:
                distx = abs(closest.x - rock.x)
                disty = abs(closest.y - rock.y)
                if rock.x < closest.x:
                    rock.x += 0.1 * distx/(distx+disty) * SPEED
                elif rock.x > closest.x:
                    rock.x -= 0.1 * distx/(distx+disty) * SPEED
                if rock.y < closest.y:
                    rock.y += 0.1 * disty/(distx+disty) * SPEED
                elif rock.y > closest.y:
                    rock.y -= 0.1 * disty/(distx+disty) * SPEED
            else:
                rock.x += 0.1 * random.randint(-1, 1) * SPEED
                rock.y += 0.1 * random.randint(-1, 1) * SPEED

        # stats
        # print("Scissors: " + str(len(self.scissors)) + " Papers: " + str(len(self.papers)) + " Rocks: " + str(len(self.rocks)))
        # print(len(self.scissors) + len(self.papers) + len(self.rocks))


        
