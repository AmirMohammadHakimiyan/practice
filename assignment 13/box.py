import arcade
class Box(arcade.Sprite):
    def __init__(self,box,x,y):
        super().__init__(box)
        self.center_x=x
        self.center_y=y
        self.width//=2
        self.height//=2



class Draw(arcade.Window):
    def __init__(self):
        super().__init__(title="loops_box")
        arcade.set_background_color(arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()
        for i in range(10):
            for b in range(10):
                if (b+i) %2==0:
                    self.min_box=Box(":resources:images/items/gemBlue.png",(i+3)*50,(b+2)*50)
                    self.min_box.draw()
                else:
                    self.min_box=Box(":resources:images/items/gemRed.png",(i+3)*50,(b+2)*50)
                    self.min_box.draw()
window=Draw()

arcade.run()
