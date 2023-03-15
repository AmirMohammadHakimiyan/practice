# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_file.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color:rgb(255, 255, 0)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Traditional Arabic"])
        font.setPointSize(27)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color:rgb(240, 0, 0)")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        font1 = QFont()
        font1.setFamilies([u"Sitka Banner"])
        font1.setPointSize(16)
        self.radioButton.setFont(font1)
        self.radioButton.setStyleSheet(u"color:red")

        self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setStyleSheet(u"color:red")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font2 = QFont()
        font2.setPointSize(25)
        self.lineEdit_2.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_4, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font2)

        self.gridLayout_4.addWidget(self.lineEdit_5, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 2, 3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb1 = QPushButton(self.centralwidget)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setFlat(True)

        self.gridLayout_2.addWidget(self.pb1, 0, 0, 1, 1)

        self.pb3 = QPushButton(self.centralwidget)
        self.pb3.setObjectName(u"pb3")
        self.pb3.setFlat(True)

        self.gridLayout_2.addWidget(self.pb3, 2, 0, 1, 1)

        self.pb4 = QPushButton(self.centralwidget)
        self.pb4.setObjectName(u"pb4")
        self.pb4.setFlat(True)

        self.gridLayout_2.addWidget(self.pb4, 3, 0, 1, 1)

        self.pb2 = QPushButton(self.centralwidget)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setFlat(True)

        self.gridLayout_2.addWidget(self.pb2, 1, 0, 1, 1)

        self.p5 = QPushButton(self.centralwidget)
        self.p5.setObjectName(u"p5")
        self.p5.setFlat(True)

        self.gridLayout_2.addWidget(self.p5, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"run", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"SLOW", None))
        self.pb1.setText("")
        self.pb3.setText("")
        self.pb4.setText("")
        self.pb2.setText("")
        self.p5.setText("")
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

