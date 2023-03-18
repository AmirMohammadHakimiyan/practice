import arcade
class Target(arcade.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.color=color
        self.width=40
        self.height=15
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
