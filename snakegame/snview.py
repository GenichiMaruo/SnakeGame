from graphics import *
from snake import Snake
from food import Food

class View:
    def __init__(self):
        self.width = 600
        self.height = 700
        self.window = GraphWin("Snake", self.width, self.height)
        self.window.setBackground("white")
        self.window.setCoords(0, 0, self.width, self.height)
        self.cercle = Circle(Point(300, 300), 290)
        self.cercle.setFill("yellow")
        self.cercle.draw(self.window)
        self.rectangle = Rectangle(Point(100, 100), Point(500, 500))
        self.rectangle.setFill("orange")
        self.rectangle.draw(self.window)
        self.text = Text(Point(300, 650), "Snake Game")
        self.text.setSize(36)
        self.text.draw(self.window)
        
    def draw(self, snake, food):
        snake.draw(self.window)
        food.draw(self.window)

    def close(self):
        self.window.close()
    
    def loop(self):
        i = 0
        while True:
            i += 1
            i = i % 6
            
            
            break