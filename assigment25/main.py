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



class T_alarm (QThread):
    my_signal=Signal(list)
    def __init__(self):
        super().__init__()
        self.all_time=[]
        self.l=[]
    def run (self):
        global list_lineedits
        while True:
            for i in self.h :
                i[0]=Time(i[2],i[3],i[4])
                i[0].minus()
                self.all_time.append([i[1],str(i[0].hour)+":"+str(i[0].minute)+":"+str(i[0].second)])
                self.h[self.h.index(i)][2]=i[0].hour
                self.h[self.h.index(i)][3]=i[0].minute
                self.h[self.h.index(i)][4]=i[0].second
            print(self.h)
            self.my_signal.emit(self.all_time)
            time.sleep(1)
            self.my_signal.emit(self.all_time)
            for a in self.h:
                print(str(self.h[self.h.index(a)][2])+":"+str(self.h[self.h.index(a)][3])+":"+str(self.h[self.h.index(a)][4]))
                print(list_lineedits[self.h[self.h.index(a)][1]].text())
                if str(self.h[self.h.index(a)][2])+":"+str(self.h[self.h.index(a)][3])+":"+str(self.h[self.h.index(a)][3])==list_lineedits[self.h[self.h.index(a)][1]].text():
                    print("salammmmmmmmmmmmm")
            del self.all_time[:]
            # time.sleep(1)
            # for k in self.all_time:
            # self.m=int(self.all_time[i][0])
            # print(list_lineedits[self.m])
            # for n in self.h:
            #     print(n)
            #     self.l=list_lineedits[self.h.index(n)][1].text().split(":")
                # print(self.h[self.h.index(n)][2])
                # print(list_lineedits[self.all_time[self.all_time.index(n)][0]].text())
                # if self.h[self.h.index(n)][2]==self.l[0] and self.h[self.h.index(n)][3]==self.l[1] and self.h[self.h.index(n)][4]==self.l[2]:
                #     print("pp")
                    # self.h[self.h.index(n)][2]=int(l[0])
                    # self.h[self.h.index(n)][3]=int(l[1])
                    # self.h[self.h.index(n)][4]=int(l[2])
                # else:
                #     print("ffffffff")
                    # self.h[self.all_time.index(n)][1]=list_lineedits[self.all_time[self.all_time.index(n)][0]].text()
            # self.my_signal.emit(self.all_time)
    def values (self,h):
        self.h=h





i=0
list_pushbuttons=[]
list_lineedits=[]
def new_alarm ():
    global i
    global list_pushbuttons
    global list_lineedits
    pushbuttons="pushbutton_"+str(i+11)
    print(pushbuttons)
    print(list_pushbuttons)
    pushbuttons=QPushButton()
    list_pushbuttons.append(pushbuttons)
    pushbuttons.setFont(QFont("Digital-7 Italic",pointSize=32))
    pushbuttons.setText("✔")
    main_window.ui.gridLayout_6.addWidget(pushbuttons,i,1)
    pushbuttons.clicked.connect(check)
    lineedits="lineedit_"+str(i+7)
    print(lineedits)
    print(list_lineedits)

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
        self.ui.pushButton_8.clicked.connect(new_alarm)


list_time=[]

def check ():
    global list_lineedits
    global mo
    global list_time
    for n in list_lineedits :
        s=n.text().replace("",".")
        mo=s.split(".")
        if len(n.text())==8 and mo[3]==":" and mo[6]==":":
            list_time.append([str(mo[1])+str(mo[2])+str(mo[4])+str(mo[5])+str(mo[7])+str(mo[8]),list_lineedits.index(n),int(str(mo[1])+str(mo[2])),int(str(mo[4])+str(mo[5])),int(str(mo[7])+str(mo[8]))])
            # list_time.append(str(mo[1])+str(mo[2]))+(str(mo[4])+str(mo[5]))+(str(mo[7])+str(mo[8]))
            # list_time.append(int(str(mo[1])+str(mo[2])))
            # list_time.append(int(str(mo[4])+str(mo[5])))
            # list_time.append(int(str(mo[7])+str(mo[8])))

            print(list_time)
        else :
            n.setText(" you should write true, for axample 00:03:20")
    thread_alarm.values(list_time)
    thread_alarm.start()


 

def slot_alarm(s):
    global list_lineedits
    global list_time

    # text=str(s.hour)+":"+str(s.minute)+":"+str(s.second)
    for i in range(len(s)) :
        # print(i)
        # print(s[i][1])
        # print(s[i][0])
        m=int(s[i][0])
        list_lineedits[m].setText(s[i][1])

           

def slot_world_clock(m):
    text=str(m.hour+4)+":"+str(m.minute)+":"+str(m.second+30)
    text_2=str(m.hour+1)+":"+str(m.minute+2)+":"+str(m.second+11)
    text_3=str(m.hour)+":"+str(m.minute+6)+":"+str(m.second+27)
    text_4=str(m.hour+7)+":"+str(m.minute+48)+":"+str(m.second+5)
    main_window.ui.lineEdit.setText("        "+text)
    main_window.ui.lineEdit_2.setText("        "+text_2)
    main_window.ui.lineEdit_3.setText("        "+text_3)
    main_window.ui.lineEdit_4.setText("        "+text_4)




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