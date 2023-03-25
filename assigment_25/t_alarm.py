import time
from PySide6.QtCore import *
from mytime import Time
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
            self.my_signal.emit(self.all_time)
            time.sleep(1)
            for a in self.h:
                h=str(self.h[self.h.index(a)][2])
                m=str(self.h[self.h.index(a)][3])
                s=str(self.h[self.h.index(a)][4])
                if len(str(self.h[self.h.index(a)][2]))==1:
                    h=str(self.h[self.h.index(a)][2])
                    h="0"+str(self.h[self.h.index(a)][2])
                if len(str(self.h[self.h.index(a)][3]))==1:
                    m=str(self.h[self.h.index(a)][3])
                    m="0"+str(self.h[self.h.index(a)][3])  
                if len(str(self.h[self.h.index(a)][4]))==1:
                    s=str(self.h[self.h.index(a)][4])
                    s="0"+str(self.h[self.h.index(a)][4])
                try:
                    if (h+":"+m+":"+s==list_lineedits[self.h[self.h.index(a)][1]].text()):
                        ...
                    else:
                        o=list_lineedits[self.h[self.h.index(a)][1]].text().split(":")
                        self.h[self.h.index(a)][2]=int(o[0])
                        self.h[self.h.index(a)][3]=int(o[1])
                        self.h[self.h.index(a)][4]=int(o[2])
                        self.h.pop(self.h.index(a))
                except:
                    ...
            del self.all_time[:]
    def values (self,h):
        del self.all_time[:]
        self.h=h