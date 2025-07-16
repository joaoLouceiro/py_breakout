class Paddle:
    def __init__(self, canvas, root, width=80, height=20, color="white"):
        self.canvas = canvas
        self.root = root
        self.canvas.update_idletasks()
        w_width = int(self.canvas.cget('width'))
        w_height = int(self.canvas.cget('height'))
        x_center = w_width // 2
        y_bottom = w_height - 20
        x1 = x_center - width // 2
        y1 = y_bottom - height
        x2 = x_center + width // 2
        y2 = y_bottom
        self.velocity = 5
        self.rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        self.w_width = w_width
        self.w_height = w_height
        self.moving_left = {'active': False, 'looping': False}
        self.moving_right = {'active': False, 'looping': False}
        self.bind_keys()

    def bind_keys(self):
        self.root.bind('<KeyPress-Left>', self.start_move_left)
        self.root.bind('<KeyRelease-Left>', self.stop_move_left)
        self.root.bind('<KeyPress-Right>', self.start_move_right)
        self.root.bind('<KeyRelease-Right>', self.stop_move_right)

    def start_move_left(self, _event):
        if not self.moving_left['active']:
            self.moving_left['active'] = True
            if not self.moving_left['looping']:
                self.moving_left['looping'] = True
                self.move_left()

    def stop_move_left(self, _event):
        self.moving_left['active'] = False

    def start_move_right(self, _event):
        if not self.moving_right['active']:
            self.moving_right['active'] = True
            if not self.moving_right['looping']:
                self.moving_right['looping'] = True
                self.move_right()

    def stop_move_right(self, _event):
        self.moving_right['active'] = False

    def move_left(self):
        if self.moving_left['active']:
            coords = self.canvas.coords(self.rect)
            left_x = coords[0]
            if left_x > 10:
                move_amount = min(self.velocity, left_x - 10)
                self.canvas.move(self.rect, -move_amount, 0)
                self.root.after(10, self.move_left)
            else:
                self.moving_left['active'] = False
                self.moving_left['looping'] = False
        else:
            self.moving_left['looping'] = False

    def move_right(self):
        if self.moving_right['active']:
            coords = self.canvas.coords(self.rect)
            right_x = coords[2]
            if right_x < self.w_width - 10:
                move_amount = min(self.velocity, self.w_width - 10 - right_x)
                self.canvas.move(self.rect, move_amount, 0)
                self.root.after(10, self.move_right)
            else:
                self.moving_right['active'] = False
                self.moving_right['looping'] = False
        else:
            self.moving_right['looping'] = False
