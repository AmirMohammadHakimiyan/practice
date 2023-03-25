import time
from PySide6.QtCore import *
from mytime import Time
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