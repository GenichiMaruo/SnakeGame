from snake import Snake
from food import Food
class Stage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(3)
        self.food = Food()
        self.food.spawn(self.snake.body)

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)