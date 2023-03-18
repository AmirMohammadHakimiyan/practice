import random
import arcade
class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x=400
        self.center_y=255
        self.change_x=random.choice([1,-1])
        self.change_y=random.choice([1,-1])
        self.radius=15
        self.width=30
        self.height=30
        self.color=arcade.color.BLACK
        self.speed=3
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,self.color)
    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed