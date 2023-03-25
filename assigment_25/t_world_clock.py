import time
from PySide6.QtCore import *
from mytime import Time
class T_world_clock (QThread):
    my_signal=Signal(Time)
    def __init__(self):
        super().__init__()
        self.mysignal =Time(0,0,0)
    def run (self):
        while True:
            self.mysignal.plus()
            self.my_signal.emit(self.mysignal)
            time.sleep(1)