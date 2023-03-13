from tkinter import *
from constants import *
from game import Game


def draw():
    canvas.delete("all")
    for scissor in g.scissors:
        canvas.create_rectangle(scissor.x-SIZE/2, scissor.y - SIZE/2, scissor.x + SIZE/2, scissor.y + SIZE/2, fill="red")
    for paper in g.papers:
        canvas.create_rectangle(paper.x-SIZE/2, paper.y - SIZE/2, paper.x + SIZE/2, paper.y + SIZE/2, fill="blue")
    for rock in g.rocks:
        canvas.create_rectangle(rock.x-SIZE/2, rock.y - SIZE/2, rock.x + SIZE/2, rock.y + SIZE/2, fill="yellow")

def update():
    draw()
    g.update()
    window.after(1000, update)

window = Tk()
window.title("Shi Fu Mi battle royale")

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

g = Game(20)
update()

window.mainloop()