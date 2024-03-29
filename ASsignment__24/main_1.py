import threading
from moviepy import editor 
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_file import Ui_MainWindow
class MainWindow(QMainWindow):
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
        self.box_2.setText("1_it can to convert 5 vidio files into audio files✔\n2_it can't convert very fast❌")
        self.box_2.show()
        for i in range(5):
            self.line[i].textChanged.connect(partial(self.edit_box,self.line[i]))
        self.ui.pushButton.clicked.connect(partial(self.run))
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
            else:
                vidio= editor.VideoFileClip(self.all_file[i])
                clip=str(i)+"_clip.mp3"
                vidio.audio.write_audiofile(clip)
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    app.exec()