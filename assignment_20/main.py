import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn1_unvisivable.setVisible(False)
        self.ui.btn2_unvisivable.setVisible(False)
        self.score1 = 0
        self.score2 = 0
        self.scoreu = 0
        self.scoret = 0
        
        self.ui.btn_onhand.clicked.connect(self.onhand)
        self.ui.btn_backhand.clicked.connect(self.backhand)
        self.ui.btn_backhand.setText("🤚")
        self.ui.btn_onhand.setText("✋")
    def computerChoice(self,user_choice):
        i = random.randint(0,1)
        if i == 0:
            self.ui.btn_computer1.setText("✋")
        else:
            self.ui.btn_computer1.setText("🤚")

            
        j = random.randint(0,1)
        if j == 0:
            self.ui.btn_computer2.setText("✋")
        else:
            self.ui.btn_computer2.setText("🤚")
        

        indwin = (user_choice + i + j)%3
        if indwin == 0:
            self.ui.how_win.setText('       no one won')
            self.scoret += 1
        elif user_choice - i - j == 1 or user_choice - i - j == -2:
            self.scoreu += 1
            self.ui.how_win.setText('       You won')
            if self.scoreu == 5:
                msg_box = QMessageBox(text= 'You are winner')
                msg_box.exec()  
                self.update_score_board(True)
        elif user_choice == j:
            self.score1 += 1
            self.ui.how_win.setText('    Computer1 won')
            if self.score1 == 5:
                msg_box = QMessageBox(text= 'Computer1 is winner')
                msg_box.exec()  
                self.update_score_board(True)
        else:
            self.score2 += 1
            self.ui.how_win.setText('    Computer2 won')
            if self.score2 == 5:
                msg_box = QMessageBox(text= 'Computer2 is winner')
                msg_box.exec()  
                self.update_score_board(True)

        self.update_score_board()
        
    def backhand(self):
        self.ui.btn_you.setText("🤚")
        self.computerChoice(1)
        
    def onhand(self):
        self.ui.btn_you.setText("✋")
        self.computerChoice(0)


    def update_score_board(self, reset = False):
        if reset:
            self.scoreu = 0
            self.score1 = 0
            self.scoret = 0
            self.score2 = 0
        self.ui.scoreboard.setText(f'Your score: {self.scoreu}    CP1s score: {self.score1}')
        self.ui.scoreboard_2.setText(f' Ties: {self.scoret}     CP2s score: {self.score2}')



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()