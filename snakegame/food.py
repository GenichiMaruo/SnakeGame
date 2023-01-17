import random
from graphics import *
from snake import Snake

class Food:
    def __init__(self, snake):
        self.x = 0
        self.y = 0
        self.color = (255, 0, 0)
        self.size = 12
        self.food = None
        self.spawn(snake)
        self.isdraw = False

    def spawn(self, snake):
        # 100~500の間で20の倍数の乱数を生成
        self.x = random.randrange(100, 500, 20)
        self.y = random.randrange(100, 500, 20)
        for segment in snake.body:
            if self.x == segment.x and self.y == segment.y:
                self.spawn(snake)
        self.isdraw = False
        if self.food is not None:
            self.food.undraw()
    
    def draw(self, window):
        if self.isdraw == False:
            self.food = Circle(Point(self.x, self.y), self.size)
            self.food.setFill(color_rgb(self.color[0], self.color[1], self.color[2]))
            self.food.setOutline(color_rgb(self.color[0], self.color[1], self.color[2]))
            self.food.draw(window)
            self.isdraw = True

    # 食べられているかどうか
    def is_eaten(self, snake):
        if self.x == snake.x and self.y == snake.y:
            return True
        return False
        