import random
import arcade
class Fruit(arcade.Sprite):
    def __init__(self,pic):
        super().__init__(pic)
        self.center_x=random.randint(0,400)*2
        self.center_y=random.randint(0,300)*2

class Apple(Fruit):
    def __init__(self,p):
        super().__init__(p)
        self.score=1
        self.height//=6
        self.width//=6


class Pear(Fruit):
    def __init__(self,p):
        super().__init__(p)
        self.score=3
        self.height//=6
        self.width//=6



class Mushroom(Fruit):
    def __init__(self,pic):
        super().__init__(pic)
        self.score=-4
        self.height//=120
        self.width//=120
