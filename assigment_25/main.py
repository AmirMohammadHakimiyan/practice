import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from main_window import Ui_MainWindow
from database import Database
from mytime import Time
from t_world_clock import T_world_clock
from t_alarm import T_alarm
# from t_timer import T_timer
# from t_stopwatch import T_stopwatch


class T_timer (QThread):
    my_signal=Signal(Time)
    def __init__(self):
        super().__init__()
        ...
    def run (self):   
        while True :
            self.timer.minus()
            text_hour=str(self.timer.hour)
            text_minute=str(self.timer.minute)
            text_second=str(self.timer.second)
            if len(str(self.timer.hour))==1:
                text_hour="0"+str(self.timer.hour)
            if len(str(self.timer.minute))==1:
                text_minute="0"+str(self.timer.minute)
            if len(str(self.timer.second))==1:
                text_second="0"+str(self.timer.second) 
            self.my_signal.emit(self.timer)
            time.sleep(1)
            pp=main_window.ui.lineEdit_6.text().replace(" ","")
            if pp==str(self.timer.hour)+":"+str(self.timer.minute)+":"+str(self.timer.second):
                ...
            else :
                return False

    def values (self,k):
        self.k=k
        self.l=self.k.split(":")
        self.h=self.l[0].replace(" ","")
        self.m=self.l[1]
        self.s=self.l[2]
        self.timer=Time(int(self.h),int(self.m),int(self.s))



class T_stopwatch(QThread):
    my_signal=Signal(Time)
    def __init__(self):
        super().__init__()
        ...
    def run (self):   
        while True :
            self.stopwatch.plus()
            text_hour=str(self.stopwatch.hour)
            text_minute=str(self.stopwatch.minute)
            text_second=str(self.stopwatch.second)
            if len(str(self.stopwatch.hour))==1:
                text_hour="0"+str(self.stopwatch.hour)
            if len(str(self.stopwatch.minute))==1:
                text_minute="0"+str(self.stopwatch.minute)
            if len(str(self.stopwatch.second))==1:
                text_second="0"+str(self.stopwatch.second) 
            self.my_signal.emit(self.stopwatch)
            time.sleep(1)
            pp=main_window.ui.lineEdit_5.text().replace(" ","")
            if pp==text_hour+":"+text_minute+":"+text_second:
                ...
            else :
                return False
    def values (self,k):
        self.k=k
        self.l=self.k.split(":")
        self.h=self.l[0].replace(" ","")
        self.m=self.l[1]
        self.s=self.l[2]
        self.stopwatch=Time(int(self.h),int(self.m),int(self.s))







i=0
list_pushbuttons=[]
list_lineedits=[]
def new_alarm ():
    global i
    global list_pushbuttons
    global list_lineedits
    pushbuttons="pushbutton_"+str(i+11)
    pushbuttons=QPushButton()
    list_pushbuttons.append(pushbuttons)
    pushbuttons.setFont(QFont("Digital-7 Italic",pointSize=32))
    pushbuttons.setText("✔")
    main_window.ui.gridLayout_6.addWidget(pushbuttons,i,1)
    pushbuttons.clicked.connect(check)

    lineedit=QLineEdit()
    lineedit.setFont(QFont("Digital-7 Italic",pointSize=32))
    list_lineedits.append(lineedit)
    main_window.ui.gridLayout_6.addWidget(lineedit,i,0)
    i+=1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global list_pushbuttons
        global list_lineedits
        global world_clock
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(new_alarm)
        self.ui.pushButton_8.clicked.connect(delete)
        self.ui.pushButton_6.clicked.connect(new_stopwatch)
        self.ui.pushButton_7.clicked.connect(delete_2)
        self.ui.pushButton_9.clicked.connect(new_timer)
        self.ui.pushButton_10.clicked.connect(delete_3)
        self.ui.pushButton_12.clicked.connect(stop)
        self.ui.pushButton_11.clicked.connect(stop)
def stop ():
    main_window.ui.lineEdit_6.setText("_"+main_window.ui.lineEdit_6.text()+"        __")      
    main_window.ui.lineEdit_5.setText("_"+main_window.ui.lineEdit_5.text()+"        __")      

def delete_3 ():
    main_window.ui.lineEdit_6.setText("            "+"00:00:00")

def new_timer ():
    M=main_window.ui.lineEdit_6.text().replace("_","")
    thread_timer.values(M)
    thread_timer.start()

def slot_timer (l):
    text=str(l.hour)+":"+str(l.minute)+":"+str(l.second)
    main_window.ui.lineEdit_6.setText("            "+text)

def new_stopwatch ():
    M=main_window.ui.lineEdit_5.text().replace("_","")
    thread_stopwatch.values(M)  
    thread_stopwatch.start()

def delete_2 ():
    main_window.ui.lineEdit_5.setText("          "+"00:00:00")

def slot_stopwatch(l):
    text_hour=str(l.hour)
    text_minute=str(l.minute)
    text_second=str(l.second)
    if len(str(l.hour))==1:
        text_hour="0"+str(l.hour)
    if len(str(l.minute))==1:
        text_minute="0"+str(l.minute)
    if len(str(l.second))==1:
        text_second="0"+str(l.second)
    text=text_hour+":"+text_minute+":"+text_second
    main_window.ui.lineEdit_5.setText("          "+text)
index_list_lineedite=0
index_list_pushbutton=0
def delete ():
    global index_list_lineedite
    global index_list_pushbutton
    global list_lineedits
    global list_pushbuttons
    hh=list_lineedits[index_list_lineedite]
    uu=list_pushbuttons[index_list_pushbutton]
    hh.deleteLater()
    uu.deleteLater()
    list_pushbuttons.pop(index_list_lineedite)
    list_lineedits.pop(index_list_lineedite)
    list_lineedits.insert(index_list_lineedite,"")
    list_pushbuttons.insert(index_list_lineedite,"")
    index_list_lineedite+=1
    index_list_pushbutton+=1


list_time=[]

def check ():
    global list_lineedits
    global mo
    global list_time
    for n in list_lineedits :
        try:
            s=n.text().replace("",".")
            mo=s.split(".")
            if len(n.text())==8 and mo[3]==":" and mo[6]==":":
                list_time.append([str(mo[1])+str(mo[2])+str(mo[4])+str(mo[5])+str(mo[7])+str(mo[8]),list_lineedits.index(n),int(str(mo[1])+str(mo[2])),int(str(mo[4])+str(mo[5])),int(str(mo[7])+str(mo[8]))])

            else :
                n.setText(" you should write true, for axample 00:03:20")
        except:
            ...
    thread_alarm.values(list_time)
    thread_alarm.start()


 

def slot_alarm(s):
    global list_lineedits
    global list_time
    for i in range(len(s)) :
        p=s[i][1].split(":")
        if len(p[0])==1:
            p[0]="0"+p[0]
        if len(p[1])==1:
            p[1]="0"+p[1]
        if len(p[2])==1:
            p[2]="0"+p[2]
        m=int(s[i][0])
        try:
            list_lineedits[m].setText(p[0]+":"+p[1]+":"+p[2])
        except:
            ...

           

def slot_world_clock(m):
    text=str(m.hour+4)+":"+str(m.minute)+":"+str(m.second)
    text_2=str(m.hour+1)+":"+str(m.minute)+":"+str(m.second)
    text_3=str(m.hour)+":"+str(m.minute)+":"+str(m.second)
    text_4=str(m.hour+7)+":"+str(m.minute)+":"+str(m.second)
    main_window.ui.lineEdit.setText("        "+text)
    main_window.ui.lineEdit_2.setText("        "+text_2)
    main_window.ui.lineEdit_3.setText("        "+text_3)
    main_window.ui.lineEdit_4.setText("        "+text_4)

thread_timer=T_timer()
thread_timer.my_signal.connect(slot_timer)
thread_stopwatch=T_stopwatch()
thread_stopwatch.my_signal.connect(slot_stopwatch)
thread_alarm=T_alarm()
thread_alarm.my_signal.connect(slot_alarm)
thread_world_clock=T_world_clock()
thread_world_clock.my_signal.connect(slot_world_clock)
thread_world_clock.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
# database=Database()
# database.add_new_Time(list_lineedits)
# database.get_Time()