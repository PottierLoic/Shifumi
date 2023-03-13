from tkinter import *
from PIL import Image, ImageTk
from constants import *
from game import Game

def draw():
    canvas.delete("all")
    for scissor in g.scissors:
        canvas.create_image(scissor.x, scissor.y, image=scissorsImg, anchor=CENTER)
    for paper in g.papers:
        canvas.create_image(paper.x, paper.y, image=paperImg, anchor=CENTER)
    for rock in g.rocks:
        canvas.create_image(rock.x, rock.y, image=rockImg, anchor=CENTER)
    g.quadtree.draw(canvas)

def frame():
    draw()
    g.update()
    window.after(1, frame)

window = Tk()
window.title("Shi Fu Mi battle royale")
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()
window.update()

rockImg = ImageTk.PhotoImage(Image.open("img/rock.png"))
paperImg = ImageTk.PhotoImage(Image.open("img/paper.png"))
scissorsImg = ImageTk.PhotoImage(Image.open("img/scissors.png"))

g = Game(300)

frame()

window.mainloop()