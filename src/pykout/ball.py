import math

class Ball:
    def __init__(self, canvas, paddle, radius=5, color="white"):
        self.canvas = canvas
        self.paddle = paddle
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
        self.dx = 2
        self.dy = 2
        self.move()

    def move(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle.rect)
        ball_left, ball_top, ball_right, ball_bottom = ball_coords
        paddle_left, paddle_top, paddle_right, paddle_bottom = paddle_coords

        # Bounce off left/right walls
        if ball_left <= 0:
            self.dx = abs(self.dx)
        if ball_right >= self.w_width:
            self.dx = -abs(self.dx)

        # Bounce off top
        if ball_top <= 0:
            self.dy = abs(self.dy)

        # Bounce off paddle
        if (
            ball_bottom >= paddle_top and
            ball_top < paddle_bottom and
            ball_right > paddle_left and
            ball_left < paddle_right and
            self.dy > 0
        ):
            hit_pos = (ball_left + ball_right) / 2 - (paddle_left + paddle_right) / 2
            norm = hit_pos / ((paddle_right - paddle_left) / 2)
            max_angle = 60  # degrees
            angle = norm * math.radians(max_angle)
            speed = (self.dx ** 2 + self.dy ** 2) ** 0.5
            self.dx = speed * math.sin(angle)
            self.dy = -abs(speed * math.cos(angle))

        # If ball hits bottom, reset to center
        if ball_bottom >= self.w_height:
            self.canvas.coords(self.ball, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
            self.dx = 2
            self.dy = 2
        self.canvas.after(10, self.move)
