import time 
import random
import arcade
import snake
import fruit
import machin


        


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height=600, title="snake")
        arcade.set_background_color(arcade.color.WARM_BLACK)
        self.number={"0":"0.png","1":"1.png","2":"2.png","3":"3.png","4":"4.png","5":"5.png","6":"6.png","7":"7.png","8":"8.png","9":"9.png"}
        self.mushroom=fruit.Mushroom("mushroom.png")
        self.bg=arcade.load_texture("BG.png")
        self.apple=fruit.Apple("apple.png")
        self.pear=fruit.Pear("pear.png")
        self.snake=snake.Snake()
        self.choice=0
    def on_draw(self):
        arcade.start_render()
        self.mushroom.draw()
        self.pear.draw()
        self.apple.draw()
        self.snake.draw()
        self.snake.game_over(self.choice)
        if int(time.time()-self.snake.time)==4:
            exit(0)
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
                self.snake.change_y=1
                self.snake.change_x=0
            if symbol==arcade.key.DOWN:
                self.snake.change_y=-1
                self.snake.change_x=0
            if symbol==arcade.key.RIGHT:
                self.snake.change_x=1
                self.snake.change_y=0
            if symbol==arcade.key.LEFT:
                self.snake.change_x=-1
                self.snake.change_y=0
    def on_update(self, delta_time: float):
        if self.choice==1:
            self.machin=machin.Machin()
            if self.snake.num_eat%2==0:
                self.machin.farman(self.snake,self.apple)
            else:
                self.machin.farman(self.snake,self.pear)
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.Eat(self.apple)
            del self.apple
            self.apple=fruit.Apple("apple.png")
        if arcade.check_for_collision(self.snake,self.pear):
            self.snake.Eat(self.pear)
            del self.pear
            self.pear=fruit.Pear("pear.png")
        if arcade.check_for_collision(self.snake,self.mushroom):
            self.snake.Eat(self.mushroom)
            del self.mushroom
            self.mushroom=fruit.Mushroom("mushroom.png")

window=Game()
arcade.run()