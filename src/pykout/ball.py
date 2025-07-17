import math
from tabulate import tabulate

from pykout.paddle import Paddle 

hit_data = []

class Ball:
    def __init__(self, canvas, paddle, blocks, radius=5, color="white"):
        self.canvas = canvas
        self.paddle = paddle
        self.blocks = blocks
        self.canvas.update_idletasks()
        self.w_width = int(self.canvas.cget('width'))
        self.w_height = int(self.canvas.cget('height'))
        self.radius = radius
        self.color = color
        self.x = self.w_width // 2
        self.y = self.w_height // 2
        self.ball = self.canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color, outline=self.color
        )
        self.dx = -3
        self.dy = 2
        self.move()

    def move(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle.rect)
        ball_left, ball_top, ball_right, ball_bottom = ball_coords
        # paddle_left, paddle_top, paddle_right, paddle_bottom = paddle_coords

        # Bounce off left/right walls
        if ball_left <= 0:
            self.dx = abs(self.dx)
        if ball_right >= self.w_width - 10:
            self.dx = -abs(self.dx)

        # Bounce off top
        if ball_top <= 0:
            self.dy = abs(self.dy)

        self.check_for_colision(self.paddle)
        for block in self.blocks:
            if not block.is_hit and self.check_for_colision(block):
                block.hit()

        # If ball hits bottom, reset to center
        if ball_bottom >= self.w_height:
            self.canvas.coords(self.ball, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
            self.dx = 2
            self.dy = 2


        self.canvas.after(10, self.move)

    def check_for_colision(self, rect):
        def is_between_sides_of_rect():
            return (
                ball_right > rect_left and
                ball_left < rect_right
                )
        def is_top_collision():
            return (
                ball_bottom >= rect_top and
                ball_top < rect_bottom and
                self.dy > 0)
                
        def is_bottom_collision():
            return (
                ball_top <= rect_bottom and
                ball_bottom > rect_top and
                self.dy < 0 and
                is_between_sides_of_rect())

        ball_coords = self.canvas.coords(self.ball)
        rect_coords = self.canvas.coords(rect.rect)
        ball_left, ball_top, ball_right, ball_bottom = ball_coords
        rect_left, rect_top, rect_right, rect_bottom = rect_coords
        if (is_top_collision() or is_bottom_collision()) and is_between_sides_of_rect():
            if type(rect) is Paddle:
                hit_pos = (ball_left + ball_right) / 2 - (rect_left + rect_right) / 2
                norm = hit_pos / ((rect_right - rect_left) / 2)
                max_angle = 60
                angle = norm * math.radians(max_angle)
                speed = (self.dx ** 2 + self.dy ** 2) ** 0.5
                new_dx = speed * math.sin(angle)
                new_dy = abs(speed * math.cos(angle))
                self.dx = new_dx
                self.dy = -new_dy if self.dy > 0 else new_dy
            else:
                self.dy = -self.dy
            return True

