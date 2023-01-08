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

class Spaceship(arcade.Sprite):
    def __init__(self,x,y,s):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=x//2
        self.center_y=y//6
        self.width//=2
        self.height//=2
        self.speed=s



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self.width,self.height,18)
        self.enemy=Enemy(self.width,self.height,2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.background)
        self.me.draw()
        self.enemy.draw()
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol ==65363:
            self.me.center_x+=self.me.speed
        elif symbol ==65361:
            self.me.center_x-=self.me.speed
    def on_update(self, delta_time: float):
        self.enemy.center_y-=self.enemy.speed
window= Game()
arcade.run()
