import sys
import urllib.request
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QDir
from ui_loader import Ui_MainWindow

class Loader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.download_btn.clicked.connect(self.download)
        self.ui.brows_btn.clicked.connect(self.brf)
    def brf(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As")
        self.ui.location.setText(QDir.toNativeSeparators(save_file[0]))
    def download(self):
        url = self.ui.url.text()
        save_location = self.ui.location.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except:
            QMessageBox.warning(self, "Warning", "The download failed.")
            return
            
        QMessageBox.information(self, "Information", "The download is complete.")
        self.ui.progress_bar.setValue(0)
        self.ui.url.setText("")
        self.ui.location.setText("")

    def report(self, block_num, block_size, total_size):
        read_sofar = block_num * block_size
        if total_size > 0:
            percent = read_sofar * 100 / total_size
            self.ui.progress_bar.setValue(int(percent))
    
    
            
app = QApplication(sys.argv)
main_window = Loader()
main_window.show()
app.exec()