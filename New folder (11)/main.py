import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from test import Ui_MainWindow
from database import Database
from mytime import Time
from t_world_clock import T_world_clock

# button=QLineEdit()
# button.setFont(QFont("Digital-7 Italic",pointSize=32))


i=0
def new_alarm ():
    global i
    global list_pushbutton
    global list_lineedit
    list_pushbutton=[]
    list_lineedit=[]
    pushbutton=QPushButton()
    pushbutton.setFont(QFont("Digital-7 Italic",pointSize=32))
    main_window.ui.gridLayout_6.addWidget(pushbutton,i,1)
    pushbutton.setText("✔")
    lineedit=QLineEdit()
    lineedit.setFont(QFont("Digital-7 Italic",pointSize=32))
    main_window.ui.gridLayout_6.addWidget(lineedit,i,0)
    list_pushbutton.append(pushbutton)
    list_lineedit.append(lineedit)
    i+=1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global list_pushbutton
        global list_lineedit
        global world_clock
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(new_alarm)
        self.thread_alarm=T_world_clock()
        self.thread_alarm.my_signal.connect(slot_alarm)
        # for n in list_pushbutton:
        #     self.ui.n.clicked.connect(check)


def check ():
    ...
    

def slot_alarm(n):
    ...
    # lineedit=QLineEdit()
    # lineedit.setFont(QFont("Digital-7 Italic",pointSize=32))
    # main_window.ui.gridLayout_6.addWidget(lineedit,0,0)
    
        

def slot_world_clock(m):
    text=str(m.hour+4)+":"+str(m.minute)+":"+str(m.second+30)
    text_2=str(m.hour+1)+":"+str(m.minute+2)+":"+str(m.second+11)
    text_3=str(m.hour)+":"+str(m.minute+6)+":"+str(m.second+27)
    text_4=str(m.hour+7)+":"+str(m.minute+48)+":"+str(m.second+5)
    main_window.ui.lineEdit.setText("        "+text)
    main_window.ui.lineEdit_2.setText("        "+text_2)
    main_window.ui.lineEdit_3.setText("        "+text_3)
    main_window.ui.lineEdit_4.setText("        "+text_4)

thread_world_clock=T_world_clock()
thread_world_clock.my_signal.connect(slot_world_clock)
thread_world_clock.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    for n in list_pushbutton:
        main_window.ui.n.clicked.connect(check)
    main_window.show()
    app.exec()