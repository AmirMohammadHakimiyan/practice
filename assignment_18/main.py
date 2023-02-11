import sys
import random
import math
from functools import partial
from PySide6.QtWidgets import QApplication ,QMessageBox
from PySide6.QtUiTools import QUiLoader
my_app= QApplication(sys.argv)



loader = QUiLoader()
my_window = loader.load("tic_toc_to.ui")

player=1
a=[]
d=[]
c=0
m=0
button=[[my_window.pushButton_1,my_window.pushButton_2,my_window.pushButton_3],
        [my_window.pushButton_4,my_window.pushButton_5,my_window.pushButton_6],
        [my_window.pushButton_7,my_window.pushButton_8,my_window.pushButton_9]]
def about ():
    box_m=QMessageBox(text=("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||WELCOME||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\t\tبازی دوز را می توان به دو شکل بازی کرد\n\t\t((((1:بازی با دستگاه2:بازی بین دو نفر))))\n\tبرای شروع بازی بر روی یکی از دکمه های زیر کلیک کنید\n\t\tplayer vs player or player vs machin\n\t\t\t\tسپس\nبا برنده شدن هریک از افراد امتیاز ان جلوی هریک از این شکلک ها قرار می گیرد\n\t\t❌:امتیاز\tor\t⭕:امتیاز\n\tو با انتخواب دکمه برگشت امتیاز ها صفر خواهد شد"))
    box_m.exec()
score_x=0
score_o=0
def win ():
    global player
    global m
    global button
    global c
    global score_x
    global score_o
    global d

    if c==0:
        for i in range(0,3,1):
            if c==0:
                for b in range(0,3,1):
                    if (button[i][0].text() in a and button[i][1].text() in a and button[i][2].text() in a) or (button[0][b].text() in a and button[1][b].text() in a and button[2][b].text() in a) or (button[i][0].text() in a and button[abs(i-1)][1].text() in a and button[abs(i-2)][2].text() in a) : 
                        score_x+=1
                        my_window.pushButton_11.setText("❌"+str(score_x))
                        c=1
                        for i in range(0,3,1):
                            for b in range(0,3,1):
                                button[i][b].setText("")
                                button[i][b].setStyleSheet("color:; background-color:;")
                                win()
                        
                        break
                    elif (button[i][0].text() in d and button[i][1].text() in d and button[i][2].text() in d) or (button[0][b].text() in d and button[1][b].text() in d and button[2][b].text() in d) or (button[i][0].text() in d and button[abs(i-1)][1].text() in d and button[abs(i-2)][2].text() in d) :
                        score_o+=1
                        my_window.pushButton_10.setText("⭕"+str(score_o))
                        c=1
                        for i in range(0,3,1):
                            for b in range(0,3,1):
                                button[i][b].setText("")
                                button[i][b].setStyleSheet("color:; background-color:;")
                                win()
                        break
    elif c==1:
        c=0
        for i in range(len(a)):
            a.pop(0)
        for i in range(len(d)):
            d.pop(0)
def again (a):
    global score_o
    global score_x
    global exit
    if a==1:
        score_o=0
        score_x=0
        for i in range(0,3,1):
            for b in range(0,3,1):
                    button[i][b].setText("")
                    button[i][b].setStyleSheet("color:; background-color:;")
        my_window.pushButton_10.setText("⭕")
        my_window.pushButton_11.setText("❌")
    elif a==2:
        for i in range(0,3,1):
            for b in range(0,3,1):
                    button[i][b].setText("")
                    button[i][b].setStyleSheet("color:; background-color:;")
        my_window.pushButton_10.setText("⭕")
        my_window.pushButton_11.setText("❌")


def play (x,y):
    global m
    global player
    global button
    global a
    global d
    g=random.choice([0,1,2])
    f=random.choice([0,1,2])
    if m==1:
        if player ==1:
            if button[x][y].text() in d or button[x][y].text() in a:
                ...
            else :
                button[x][y].setStyleSheet("color:red; background-color: orange;")
                button[x][y].setText("x")
                a.append(button[x][y].text())
                player=2
                win()
        
                
        elif player==2:
            if button[x][y].text() in a or button[x][y].text() in d:
                ...
            else :
                button[x][y].setStyleSheet("color:blue; background-color: purple;")
                button[x][y].setText("o")
                d.append(button[x][y].text())
                player=1
                win()
    elif m==2:
        if player ==1:
            if button[x][y].text() in d or button[x][y].text() in a:
                ...
            else :
                button[x][y].setStyleSheet("color:red; background-color: orange;")
                button[x][y].setText("x")
                a.append(button[x][y].text())
                play(x,y)
                player=2
                win()
        elif player==2:
            if button[g][f].text() in d or button[g][f].text() in a: 
                play(x,y)
                g=random.choice([0,1,2])
                f=random.choice([0,1,2])
            else:
                button[g][f].setStyleSheet("color:blue; background-color: purple;")
                button[g][f].setText("o")
                d.append(button[g][f].text())
                player=1
                win()
    if len(a)+len(d)==9:
        again(2)

def typ_game(a):
    global m
    if a==1:
        m=1
    elif a==2:
        m=2

for i in range(0,3,1):
    for b in range(0,3,1):
        button[i][b].clicked.connect(partial(play, i, b))
my_window.pushButton_12.clicked.connect(partial(again,1))
my_window.radioButton.clicked.connect(partial(typ_game,1))
my_window.radioButton_2.clicked.connect(partial(typ_game,2))
my_window.pushButton.clicked.connect(partial(about))


my_window.show()
my_app.exec()