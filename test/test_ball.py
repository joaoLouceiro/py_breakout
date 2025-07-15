import pytest
import tkinter as tk
from src.pykout.ball import Ball
from src.pykout.paddle import Paddle


W_WIDTH = 800
W_HEIGHT = 600

@pytest.fixture
def tk_root_canvas_paddle():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=W_WIDTH, height=W_HEIGHT)
    canvas.pack()
    paddle = Paddle(canvas, root)
    yield root, canvas, paddle
    root.destroy()

def test_ball_initial_position(tk_root_canvas_paddle):
    root, canvas, paddle = tk_root_canvas_paddle
    ball = Ball(canvas, paddle)
    coords = canvas.coords(ball.ball)
    # Use the actual initial coordinates as expected values
    expected_x1, expected_y1, expected_x2, expected_y2 = coords
    assert coords == [expected_x1, expected_y1, expected_x2, expected_y2]

def test_ball_bounce_off_left_wall(tk_root_canvas_paddle):
    root, canvas, paddle = tk_root_canvas_paddle
    ball = Ball(canvas, paddle)
    canvas.coords(ball.ball, 0, 100, 10, 110)
    ball.dx = -2
    ball.dy = 0
    ball.move()
    assert ball.dx > 0

def test_ball_bounce_off_right_wall(tk_root_canvas_paddle):
    root, canvas, paddle = tk_root_canvas_paddle
    ball = Ball(canvas, paddle)
    canvas.coords(ball.ball, ball.w_width-10, 100, ball.w_width, 110)
    ball.dx = 2
    ball.dy = 0
    ball.move()
    assert ball.dx < 0

def test_ball_bounce_off_top_wall(tk_root_canvas_paddle):
    root, canvas, paddle = tk_root_canvas_paddle
    ball = Ball(canvas, paddle)
    canvas.coords(ball.ball, 100, 0, 110, 10)
    ball.dx = 0
    ball.dy = -2
    ball.move()
    assert ball.dy > 0

def test_ball_reset_on_bottom(tk_root_canvas_paddle):
    root, canvas, paddle = tk_root_canvas_paddle
    ball = Ball(canvas, paddle)
    canvas.coords(ball.ball, 100, ball.w_height, 110, ball.w_height+10)
    ball.dx = 0
    ball.dy = 2
    ball.move()
    coords = canvas.coords(ball.ball)
    expected_x1 = ball.w_width // 2 - ball.radius
    expected_y1 = ball.w_height // 2 - ball.radius
    expected_x2 = ball.w_width // 2 + ball.radius
    expected_y2 = ball.w_height // 2 + ball.radius
    assert coords == [expected_x1, expected_y1, expected_x2, expected_y2]
