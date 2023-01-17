from snview import View
from snake import Snake
from food import Food

def main():
    view = View()
    snake = Snake(100,100,4,1)
    food = Food(snake)
    key = None
    try:
        for i in range(1000):
            view.draw(snake, food)
            key = view.window.checkKey()
            if key == "q":
                break
            else:
                snake.move(key)
                if food.is_eaten(snake):
                    food.spawn(snake)
                    snake.eat()
            # 1/6秒待つ
            view.window.after(1000//6)
    except Exception as e:
        view.gameover()
        view.window.getMouse()
    finally:
        view.close()

if __name__ == "__main__":
    main()