import time
from PySide6.QtCore import *
from mytime import Time
from main import *
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