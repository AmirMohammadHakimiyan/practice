import arcade

class Enemy():
    ...
class Spaceship(arcade.sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=x
        self.center_y=y



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.background)
        self.me.draw()
window= Game()
arcade.run()
