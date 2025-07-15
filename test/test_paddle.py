import pytest
import tkinter as tk
from src.pykout.paddle import Paddle

W_WIDTH = 800
W_HEIGHT = 600

@pytest.fixture
def tk_root_and_canvas():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=W_WIDTH, height=W_HEIGHT)
    canvas.pack()
    yield root, canvas
    root.destroy()

def test_paddle_initial_position(tk_root_and_canvas):
    root, canvas = tk_root_and_canvas
    paddle = Paddle(canvas, root)
    coords = canvas.coords(paddle.rect)
    expected_x1 = W_WIDTH // 2 - 60 // 2
    expected_y1 = W_HEIGHT - 20 - 20
    expected_x2 = W_WIDTH // 2 + 60 // 2
    expected_y2 = W_HEIGHT - 20
    assert coords == [expected_x1, expected_y1, expected_x2, expected_y2]

def test_paddle_move_left_stops_at_left_edge(tk_root_and_canvas):
    root, canvas = tk_root_and_canvas
    paddle = Paddle(canvas, root)
    # Move paddle to the left edge
    for _ in range(100):
        paddle.moving_left['active'] = True
        paddle.move_left()
    coords = canvas.coords(paddle.rect)
    assert coords[0] == 10

def test_paddle_move_right_stops_at_right_edge(tk_root_and_canvas):
    root, canvas = tk_root_and_canvas
    paddle = Paddle(canvas, root)
    # Move paddle to the right edge
    for _ in range(200):
        paddle.moving_right['active'] = True
        paddle.move_right()
    coords = canvas.coords(paddle.rect)
    assert coords[2] == 790
