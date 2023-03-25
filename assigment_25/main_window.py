# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 687)
        icon = QIcon()
        icon.addFile(u"../New folder (10)/\u0648\u06a9\u062a\u0648\u0631-\u0637\u0631\u062d-\u0627\u0646\u062a\u0632\u0627\u0639\u06cc-\u0646\u0642\u0634\u0647-\u0632\u0645\u06cc\u0646.jpg", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u"../New folder (10)/\u0648\u06a9\u062a\u0648\u0631-\u0637\u0631\u062d-\u0627\u0646\u062a\u0632\u0627\u0639\u06cc-\u0646\u0642\u0634\u0647-\u0632\u0645\u06cc\u0646.jpg", QSize(), QIcon.Active, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        MainWindow.setIconSize(QSize(150, 138))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Algerian"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Digital-7 Italic"])
        font1.setPointSize(72)
        font1.setItalic(True)
        self.lineEdit_3.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setCursorPosition(8)

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font2 = QFont()
        font2.setFamilies([u"Digital-7 Italic"])
        font2.setPointSize(36)
        font2.setItalic(True)
        self.pushButton_8.setFont(font2)

        self.gridLayout_4.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)

        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayout = QFormLayout(self.tab_3)
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font3 = QFont()
        font3.setFamilies([u"Digital-7 Italic"])
        font3.setPointSize(28)
        font3.setItalic(True)
        self.pushButton_6.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_6)

        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_7)

        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_5)

        self.pushButton_11 = QPushButton(self.tab_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_11)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_6 = QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font1)

        self.gridLayout_5.addWidget(self.lineEdit_6, 4, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.tab_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font3)

        self.gridLayout_5.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font3)

        self.gridLayout_5.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.tab_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font3)

        self.gridLayout_5.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"  00:00 ", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"  00:00 ", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"  00:00 ", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"  00:00 ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"WORLD", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"US", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"IRAN", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"GERMANY", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"world_clock", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"ALARM", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"          00:00:00", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"STOP_WATCH", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"          00:00:00", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"TIMER", None))
    # retranslateUi

