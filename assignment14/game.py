import arcade
import random
import time
import spaceship
import enemy
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.new_bg=arcade.load_texture("Untitled112.png")
        self.new_bg2=arcade.load_texture("win.jpg")
        self.me=spaceship.Spaceship(self.width,self.height,10)
        self.enemy=enemy.Enemy(self.width,self.height,2)
        self.coin=spaceship.Coin(self.width,self.height)
        self.sc=0
        self.line=[]
        self.doshmans=[]
        self.seconds=time.time()
        self.set=3
        self.sound_enemy=arcade.load_sound(":resources:sounds/explosion1.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.background)
        self.me.draw()
        for self.he in self.me.hearts:
            self.he.draw()
        for self.doshman in self.doshmans:
            self.doshman.draw()
        for self.bullet in self.me.bullets:
            self.bullet.draw()
        for self.ml in self.line:
            self.ml.draw()
        self.coin.draw()
        if self.me.Game_over()=="lose":
            arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.new_bg)
        if self.me.Win(self.line)=="Win":
            arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.new_bg2)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol ==arcade.key.RIGHT:
            self.me.change_x=1
        elif symbol ==arcade.key.LEFT:
            self.me.change_x=-1
        elif symbol==arcade.key.SPACE:
            self.me.Shotting()
        elif symbol ==arcade.key.DOWN:
            self.me.change_x=0
    def on_update(self, delta_time: float):
        self.me.move()
        if int(time.time()-self.seconds)%3==0 and int(time.time()-self.seconds)==self.set:
            self.set+=3
            self.new_dosh=enemy.Enemy(self.width,self.height,5)
            self.doshmans.append(self.new_dosh)
        for b in self.me.bullets:
            for e in self.doshmans:
                if arcade.check_for_collision(b,e):
                    self.doshmans.remove(e)
                    self.me.bullets.remove(b)
                    arcade.play_sound(self.sound_enemy)
                    self.sc+=1
        for doshman in self.doshmans:
            if arcade.check_for_collision(self.me,doshman):
                self.me.hearts.clear()
            elif len(self.me.hearts)>0 and doshman.center_y<0:
                self.me.hearts.pop(0)
                self.doshmans.remove(doshman)
        for self.bullet in self.me.bullets:
            self.bullet.center_y+=self.bullet.speed
            self.line.clear()
        self.m=0
        for i in range(self.sc):
            if i>5:
                self.new_line=spaceship.Score(self.width-((i-6)*15),self.height-50)
                self.line.append(self.new_line)
                self.m+=1
            else:
                self.new_line=spaceship.Score(self.width-(i*15),self.height)
                self.line.append(self.new_line)
                self.m+=1
        for self.doshman in self.doshmans:
            self.doshman.move(self.m)



window= Game()
arcade.run()
