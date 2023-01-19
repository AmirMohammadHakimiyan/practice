import arcade 
import random
class Machin():
    def __init__(self):
        ...
    def farman(self,snake,food):
        if abs(food.center_x-snake.center_x)>10 and snake.center_x<food.center_x:
            snake.hange_x=1
            snake.hange_y=0
        elif abs(snake.center_x-food.center_x)>10 and snake.center_x>food.center_x:
            snake.hange_y=0
            snake.hange_x=-1
        elif snake.center_y>food.center_y and abs(snake.center_x-food.center_x)<=10:
            snake.hange_y=-1
            snake.hange_x=0
        elif snake.center_y<food.center_y and abs(snake.center_x-food.center_x)<=10:
            snake.hange_y=1
            snake.hange_x=0
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

class Fake(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("apple.png")
        self.center_x=x
        self.center_y=y



class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x=random.randint(0,400)*2
        self.center_y=random.randint(0,300)*2
        self.width=40
        self.height=40
        self.hange_x=0
        self.hange_y=0
        self.speed=3
        self.score=2
        self.body=[]
        self.num=1
        self.num_eat=0
        self.color=arcade.color.ORANGE
    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})
        if len(self.body)>self.score:
            self.body.pop(0)
        self.center_x+=self.hange_x*self.speed
        self.center_y+=self.hange_y*self.speed
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y,10, arcade.color.AFRICAN_VIOLET)
        for i in self.body:
            self.num+=1
            if self.num%2==0:
                arcade.draw_rectangle_filled(i["x"],i["y"],20,20,arcade.color.AMARANTH_PINK)
            else:
                arcade.draw_rectangle_filled(i["x"],i["y"],20,20,arcade.color.AQUA)
        # for i in self.body:
        #     self.fake=Fake(i["x"],i["y"])
        #     if arcade.check_for_collision(self,self.fake):
        #         if self.body.index(i) > len(self.body)-30:
        #             ...
        #         else:
        #             self.score=-1
        # for i in self.body:
            # for b in self.body[0:len(self.body)-5]: 
            #     if b["x"]==i["x"] and b["y"]==i["y"]:
            #         self.b=Fake(b["x"],b["y"])
            #         if arcade.check_for_collision(self,self.b):
            #             self.score=-1
    def Eat(self,food):
        print(self.score)
        self.num_eat+=1
        self.score+=food.score
        if food.score>0:
            self.body.append({"x":self.center_x,"y":self.center_y})
        else :
            self.body.pop(0)
    def game_over(self):
        if self.score<0:
            self.over=arcade.load_texture("REN.png")
            arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.over)
        # for i in self.body:
        #     for b in self.body[0:len(self.body)-5]: 
        #         if b["x"]==i["x"] and b["y"]==i["y"]:
        #             self.b=Fake(b["x"],b["y"])
        #             if arcade.check_for_collision(self,self.b):
        #                 self.score=-1
        



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height=600, title="snake")
        arcade.set_background_color(arcade.color.WARM_BLACK)
        self.number={"0":"0.png","1":"1.png","2":"2.png","3":"3.png","4":"4.png","5":"5.png","6":"6.png","7":"7.png","8":"8.png","9":"9.png"}
        self.mushroom=Mushroom("mushroom.png")
        self.bg=arcade.load_texture("BG.png")
        self.apple=Apple("apple.png")
        self.pear=Pear("pear.png")
        self.snake=Snake()
        self.choice=0
    def on_draw(self):
        arcade.start_render()
        self.mushroom.draw()
        self.pear.draw()
        self.apple.draw()
        self.snake.draw()
        self.snake.game_over()
        if self.snake.score>=0:
            self.n=str(self.snake.score).replace("",",")
            self.m=self.n.split(",")
            for i in self.m:
                if i !="":
                    self.shape=arcade.load_texture(self.number[i])
                    arcade.draw_lrwh_rectangle_textured(self.m.index(i)*40,0,40,40,self.shape)
        if self.choice==0:
            arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.bg)
        arcade.finish_render()
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.KEY_1:
            self.choice=1
        elif symbol==arcade.key.KEY_2:
            self.choice=2
        if self.choice==2:
            if symbol==arcade.key.UP:
                self.snake.hange_y=1
                self.snake.hange_x=0
            if symbol==arcade.key.DOWN:
                self.snake.hange_y=-1
                self.snake.hange_x=0
            if symbol==arcade.key.RIGHT:
                self.snake.hange_x=1
                self.snake.hange_y=0
            if symbol==arcade.key.LEFT:
                self.snake.hange_x=-1
                self.snake.hange_y=0
    def on_update(self, delta_time: float):
        if self.choice==1:
            self.machin=Machin()
            if self.snake.num_eat%2==0:
                self.machin.farman(self.snake,self.apple)
            else:
                self.machin.farman(self.snake,self.pear)
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.Eat(self.apple)
            del self.apple
            self.apple=Apple("apple.png")
        if arcade.check_for_collision(self.snake,self.pear):
            self.snake.Eat(self.pear)
            del self.pear
            self.pear=Pear("pear.png")
        if arcade.check_for_collision(self.snake,self.mushroom):
            self.snake.Eat(self.mushroom)
            del self.mushroom
            self.mushroom=Mushroom("mushroom.png")
        for i in self.snake.body:
            self.fake=Fake(i["x"],i["y"])
            if arcade.check_for_collision(self.snake,self.fake):
                if self.snake.body.index(i) > len(self.snake.body)-30:
                    ...
                else:
                    self.snake.score=-1
window=Game()
arcade.run()
