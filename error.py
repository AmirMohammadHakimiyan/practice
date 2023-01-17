mport arcade 
import random
class Machin():
    def __init__(self,fruit,snake):
        self.snake_x=snake.center_x
        self.snake_y=snake.center_y
        self.fruit_x=fruit.center_x
        self.fruit_y=fruit.center_y

    def farmon(self):
        if self.snake_x>self.fruit_x:
            self.far=-1
        else:
            self.far=1
        if self.snake_y>self.fruit_y:
            self.far2=-1
        else:
            self.far2=1


class Fruit(arcade.Sprite):
    def __init__(self,pic):
        super().__init__(pic)
        self.center_x=random.randint(0,1200)
        self.center_y=random.randint(0,800)

class Apple(Fruit):
    def __init__(self,p):
        super().__init__(p)
        self.score=1
        self.height//=6
        self.width//=6


class Pear(Fruit):
    def __init__(self,p):
        super().__init__(p)
        self.score=2
        self.height//=6
        self.width//=6



class Mushroom(Fruit):
    def __init__(self,pic):
        super().__init__(pic)
        self.score=-1
        self.height//=120
        self.width//=120



class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.score=10
        self.center_x=400
        self.center_y=300
        self.change_x=0
        self.change_y=0
        self.speed=8
        self.color=arcade.color.AMBER
        self.body=[]
        self.num=1
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,60,60,self.color)
        for i in self.body:
            self.num+=1
            if self.num%2==0:
                arcade.draw_rectangle_filled(i["x"],i["y"],60,60,self.color)
            else:
                arcade.draw_rectangle_filled(i["x"],i["y"],60,60,arcade.color.AQUA)
    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})
        if len(self.body)>self.score:
            self.body.pop(0)
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed
    def eat(self,food):
        self.score+=food.score
        self.body.append({"x":self.center_x,"y":self.center_y})


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 1200, height= 800, title="snake")
        arcade.set_background_color(arcade.color.WARM_BLACK)
        self.mushroom=Mushroom("mushroom.png")
        self.apple=Apple("apple.png")
        self.pear=Pear("pear.png")
        self.snake=Snake()
        self.num=1
    def on_draw(self):
        arcade.start_render()
        self.mushroom.draw()
        self.snake.draw()
        self.pear.draw()
        self.apple.draw()
    def on_update(self, delta_time: float):
        self.machin=Machin(self.apple,self.snake)
        self.machin.farmon()
        self.snake.change_x=self.machin.far
        self.snake.change_y=self.machin.far2
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat(self.apple)
            del self.apple
            self.apple=Apple("apple.png")
        if arcade.check_for_collision(self.snake,self.pear):
            self.snake.eat(self.pear)
            del self.pear
            self.pear=Pear("pear.png")
        elif arcade.check_for_collision(self.snake,self.mushroom):
            self.snake.eat(self.mushroom)
            del self.mushroom
            self.mushroom=Mushroom("mushroom.png")
window=Game()
arcade.run()
