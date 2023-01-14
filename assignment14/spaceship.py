import arcade
class Score(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("Untitledsc.png")
        self.center_x=x-30
        self.center_y=y-15
        self.width//=60
        self.height//=60
        self.angle=90
class Heart(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("heart.jpg")
        self.center_x=x
        self.center_y=y
        self.height//=8
        self.width//=8
class Coin(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(":resources:images/items/coinGold.png")
        self.center_x=x-15
        self.center_y=y-15
        self.width//=4
        self.height//=4
class Bullet(arcade.Sprite):
    def __init__(self,x,y,s):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x=x
        self.center_y=y+15
        self.speed=s
class Spaceship(arcade.Sprite):
    def __init__(self,x,y,s):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.x=x
        self.center_x=x//2
        self.center_y=y//6
        self.width//=2
        self.height//=2
        self.speed=s
        self.change_x=0
        self.hearts=[]
        self.bullets=[]
        self.game="continue"
        self.h=Heart((x-10),y//10)
        self.h1=Heart((x-40),y//10)
        self.h2=Heart((x-70),y//10)
        self.hearts.append(self.h)
        self.hearts.append(self.h1)
        self.hearts.append(self.h2)
    def move(self):
        if self.change_x==1 and self.center_x< self.x:
            self.center_x+=self.speed
        elif self.change_x==-1 and self.center_x>0:
            self.center_x-=self.speed
    def Shotting(self):
        self.bullet=Bullet(self.center_x,self.center_y,60)
        self.bullets.append(self.bullet)
    def Game_over(self):
        if len(self.hearts)==0:
            return "lose"
    def Win(self,line):
        if line==10:
            return "Win"
