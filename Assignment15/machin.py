class Machin():
    def __init__(self):
        ...
    def farman(self,snake,food):
        if abs(food.center_x-snake.center_x)>10 and snake.center_x<food.center_x:
            snake.change_x=1
            snake.change_y=0
        elif abs(snake.center_x-food.center_x)>10 and snake.center_x>food.center_x:
            snake.change_y=0
            snake.change_x=-1
        elif snake.center_y>food.center_y and abs(snake.center_x-food.center_x)<=10:
            snake.change_y=-1
            snake.change_x=0
        elif snake.center_y<food.center_y and abs(snake.center_x-food.center_x)<=10:
            snake.change_y=1
            snake.change_x=0