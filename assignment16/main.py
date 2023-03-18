import arcade
import ball
import target
import raket
class Game(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.raket=raket.Raket(self)
        self.targets=[]
        for i in range(13):
            self.target=target.Target(arcade.color.ORANGE,(i+0.5)*60,350)
            self.target2=target.Target(arcade.color.RED,(i+0.5)*60,380)
            self.target3=target.Target(arcade.color.PURPLE_TAUPE,(i+0.5)*60,410)
            self.targets.append(self.target)
            self.targets.append(self.target2)
            self.targets.append(self.target3)
            self.ball=ball.Ball()
            self.nbg=arcade.load_texture("win.png")
            self.number={"0":"0.png","1":"1.png","2":"2.png","3":"3.png","4":"4.png","5":"5.png","6":"6.png","7":"7.png","8":"8.png","9":"9.png"}
    def on_draw(self):
        arcade.start_render()
        self.raket.draw()
        for i in self.targets:
            i.draw()
        self.ball.draw()
        self.ra=str(self.raket.score).replace("",",")
        self.scores=self.ra.split(",")
        
        self.bn=arcade.load_texture(self.number[self.scores[1]])
        arcade.draw_lrwh_rectangle_textured(20,300,20,20,self.bn)
        if len(self.scores)==4:
            self.b=arcade.load_texture(self.number[self.scores[2]])
            arcade.draw_lrwh_rectangle_textured(35,300,20,20,self.b)
        if len(self.scores)==5:
            self.b=arcade.load_texture(self.number[self.scores[2]])
            arcade.draw_lrwh_rectangle_textured(35,300,20,20,self.b)
            self.x=arcade.load_texture(self.number[self.scores[3]])
            arcade.draw_lrwh_rectangle_textured(55,300,20,20,self.x)
        if len(self.raket.hearts)==0:
            self.game_over=arcade.load_texture("LOSE.png")
            arcade.draw_lrwh_rectangle_textured(0,0,800,600,self.game_over)
        if self.ball.center_y>600:
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.nbg)
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.raket.change_x=1
        if symbol ==arcade.key.LEFT:
            self.raket.change_x=-1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.raket.center_x=x
    def on_update(self, delta_time: float):
        self.raket.move()
        for n in self.targets:
            if arcade.check_for_collision(n,self.ball):
                self.targets.remove(n)
                self.ball.change_y*=-1
                self.raket.score+=4
        if arcade.check_for_collision(self.raket,self.ball):
            self.ball.change_y*=-1
        if self.ball.center_x>self.width or self.ball.center_x<0:
            self.ball.change_x*=-1
        if self.ball.center_y<0:
            del self.ball
            self.ball=ball.Ball()
            if len(self.raket.hearts)>0:
                self.raket.hearts.pop(0)
        self.ball.move()


window=Game()
arcade.run()
