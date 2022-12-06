class snake:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.body = []
        self.body.append((x, y))

    def move(self):
        pass

    def draw(self, surface):
        pass

    def eat(self, food):
        pass

    def collision(self):
        pass