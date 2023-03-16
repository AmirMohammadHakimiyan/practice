import random
import threading
from moviepy import editor 
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_file import Ui_MainWindow
class My_thread(QThread):
    qwee=Signal()
    def __init__(self,lt):
        super().__init__()
        self.path=lt

    def run(self):
        video=editor.VideoFileClip(self.path)
        self.name=str(random.randint(0,10000000000))+"_clip.mp3"
        video.audio.write_audiofile(self.name)
        self.qwee.emit()
        
class MainWindow(QMainWindow):
    read=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.line=[self.ui.lineEdit,self.ui.lineEdit_2,self.ui.lineEdit_3,self.ui.lineEdit_4,self.ui.lineEdit_5]
        self.all_file=[]
        self.box=QMessageBox()
        self.box.setWindowTitle("⚠")
        self.box.setText("plesse, complte all of them!😎")
        self.box_2=QMessageBox()
        self.box_2.setWindowTitle("***ABOUT***")
        self.box_2.setText("1_it can to convert 5 vidio files into audio files✔\n2_it can convert very fast✔")
        self.box_2.show()
        for i in range(5):
            self.line[i].textChanged.connect(partial(self.edit_box,self.line[i]))
        self.ui.pushButton.clicked.connect(partial(self.run))
        self.number_1=0
        self.number_2=0
    def edit_box(self,m,n):
        if len(m.text())<3:
            file_path=QFileDialog.getOpenFileName(self,"choce your file!")
            c=str(file_path).split("', 'All Files (*)'")
            v=c[0]
            n=str(v).split("('")
            n_2=n[1]
            m.setText(str(n_2))
            self.all_file.append(str(n_2))
    def run(self):
        for i in range(5):
            if self.line[i].text()=="":
                self.box.show()
                self.number_1+=1
            else:
                self.number_2+=1
                if self.number_2==5 and self.number_1==0:
                    self.read.emit(self.all_file)
        self.number_1=0
        self.number_2=0
                    
def maker(lt):
    global th
    th=My_thread(lt[0])
    th_2=My_thread(lt[1])
    th_3=My_thread(lt[2])
    th_4=My_thread(lt[3])
    th_5=My_thread(lt[4])
    th_3.start()
    th_4.start()
    th_5.start()
    th_2.start()
    th.start()

    th_2.qwee.connect(th_2.quit)
    th_3.qwee.connect(th_3.quit)
    th_4.qwee.connect(th_4.quit)
    th_5.qwee.connect(th_5.quit)
    th.qwee.connect(th.quit)
    th_2.wait()
    th_3.wait()
    th_4.wait()
    th_5.wait()
    th.wait()

if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.read.connect(maker)

    window.show()
    app.exec()