class Block:
    def __init__(self, canvas, x, y, color="white", width=60, height=20) -> None:
        self.canvas = canvas
        x1 = x - width / 2
        x2 = x + width / 2
        y1 = y - height / 2
        y2 = y + height / 2
        self.rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        self.is_hit = False

    def hit(self):
        self.is_hit = True
        self.canvas.delete(self.rect)
