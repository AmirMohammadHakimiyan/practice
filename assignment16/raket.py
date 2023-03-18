import arcade
class Heart(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("heart.png")
        self.center_x=x
        self.center_y=y
        self.width//=70
        self.height//=70
class Raket(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.score=0
        self.color=arcade.color.PALE_GOLD
        self.center_x=game.width//2
        self.center_y=game.height//10
        self.width=40
        self.height=10
        self.speed=6
        self.change_x=0
        self.change_y=0
        self.heart=Heart(20,15)
        self.heart2=Heart(20,50)
        self.heart3=Heart(20,85)
        self.hearts=[self.heart,self.heart2,self.heart3]
    def draw(self):
        for i in self.hearts:
            i.draw()
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
    def move(self):
        if self.center_x<self.game.width-20 and self.change_x!=-1:
            self.center_x+=self.change_x*self.speed
        if self.center_x>20 and self.change_x!=1:
            self.center_x+=self.change_x*self.speed
