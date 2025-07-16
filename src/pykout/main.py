import tkinter as tk
from random import choice
from pykout.paddle import Paddle
from pykout.ball import Ball
from pykout.block import Block

W_WIDTH = 800
W_HEIGHT = 600
BLOCKS_PER_LINE = 10
ROWS_OF_BLOCKS = 6

def create_main_window(width, height):
    root = tk.Tk()
    root.title("PyBreakout")
    root.configure(bg="black", width=width, height=height)
    canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0, bg="black")
    canvas.place(x=0, y=0)
    paddle = Paddle(canvas, root)
    block_width = W_WIDTH / BLOCKS_PER_LINE
    block_array = []
    for j in range (0, ROWS_OF_BLOCKS + 0):
        color = choice(["red", "green", "orange", "blue"])
        y_pos = W_HEIGHT / 8 + 30 * j
        for i in range(1, BLOCKS_PER_LINE + 1):
            x_pos = (block_width * i) - block_width / 2
            block_array.append(Block(canvas, x=x_pos, y=y_pos, color=color))

    ball = Ball(canvas, paddle, block_array)
    canvas.pack()
    return root

window = create_main_window(width=W_WIDTH, height=W_HEIGHT)

window.mainloop()
