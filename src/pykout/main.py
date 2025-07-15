import tkinter as tk
from pykout.paddle import Paddle
from pykout.ball import Ball

W_WIDTH = 800
W_HEIGHT = 600

def create_main_window(width, height):
    root = tk.Tk()
    root.title("PyBreakout")
    root.configure(bg="black", width=width, height=height)
    canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0, bg="black")
    canvas.place(x=0, y=0)
    paddle = Paddle(canvas, root)
    ball = Ball(canvas, paddle)
    return root

window = create_main_window(width=W_WIDTH, height=W_HEIGHT)

window.mainloop()
