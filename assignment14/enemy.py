import arcade
import random
class Enemy(arcade.Sprite):
    def __init__(self,w,y,s):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x=random.randint(0,w)
        self.center_y=y-10
        self.width//=2
        self.height//=2
        self.angle=180
        self.speed=s
    def move(self,score):
        if score<2 :
            self.center_y-=self.speed
        elif score>1 and score<5:
            self.center_y-=self.speed+2
        elif score>4 and score<8:
            self.center_y-=self.speed+3
        elif score>7:
            self.center_y-=self.speed*3