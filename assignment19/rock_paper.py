import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.setText("🧱")
        self.ui.pushButton_2.setText("🧻")
        self.ui.pushButton_3.setText("✂")
        self.ui.pushButton_7.setText("your score:")
        self.ui.score1.setText("machins score:")
        self.ui.pushButton_4.setText("🧱")
        self.ui.pushButton_5.setText("🧻")
        self.ui.pushButton_6.setText("✂")
        self.score=0
        self.score_ma=0
        self.buttons=[self.ui.pushButton_4,self.ui.pushButton_5,self.ui.pushButton_6]
        self.buttons_ma=[self.ui.pushButton,self.ui.pushButton_2,self.ui.pushButton_3]
        for i in range(0,3,1):
            self.buttons[i].clicked.connect(partial(self.play,i))
    def play (self,x):
        self.ui.pushButton.setText("🧱")
        self.ui.pushButton_2.setText("🧻")
        self.ui.pushButton_3.setText("✂")
        self.machin=random.randint(0,3)
        self._x=x
        if self._x==0:
            
            
            if self.machin==0:
                self.mosavi()
            elif self.machin==1:
                self.bakht()
            elif self.machin==2:
                self.bord()
        elif self._x==1:
            
            
            if self.machin==1:
                self.mosavi()
            elif self.machin==0:
                self.bord()
            elif self.machin==2:
                self.bakht()
        elif self._x==2:
            
            
            if self.machin==2:
                self.mosavi()
            elif self.machin==0:
                self.bakht()
            elif self.machin==1:
                self.bord
    def mosavi (self):
        self.buttons_ma[self.machin].setText("👀")
    def bord (self):
        self.score+=1
        self.ui.pushButton_7.setText("your score:"+str(self.score))
        self.ui.score1.setText("machins score:"+str(self.score_ma))
        self.buttons_ma[self.machin].setText("👀")
    def bakht(self):
        self.score_ma+=1
        self.ui.pushButton_7.setText("your score:"+str(self.score))
        self.ui.score1.setText("machins score:"+str(self.score_ma))
        self.buttons_ma[self.machin].setText("👀")



my_app = QApplication(sys.argv)
window = MainWindow()
window.show()
my_app.exec()



    