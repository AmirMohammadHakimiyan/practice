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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 422)
        icon = QIcon()
        icon.addFile(u"todo-list-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 17, 0);")
        MainWindow.setIconSize(QSize(100, 100))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        font = QFont()
        font.setPointSize(15)
        self.tb_new_task_title.setFont(font)
        self.tb_new_task_title.setStyleSheet(u"background-color: rgb(0, 170, );")

        self.verticalLayout.addWidget(self.tb_new_task_title)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setMaximumSize(QSize(16777215, 100))
        self.tb_new_task_description.setFont(font)
        self.tb_new_task_description.setStyleSheet(u"background-color: rgb(0, 170, );")

        self.verticalLayout.addWidget(self.tb_new_task_description)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cb_priority = QCheckBox(self.centralwidget)
        self.cb_priority.setObjectName(u"cb_priority")
        font1 = QFont()
        font1.setFamilies([u"Centaur"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.cb_priority.setFont(font1)

        self.verticalLayout.addWidget(self.cb_priority)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font2 = QFont()
        font2.setPointSize(12)
        self.dateTimeEdit.setFont(font2)
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(0, 110, 0);")

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.btn_newtask = QPushButton(self.centralwidget)
        self.btn_newtask.setObjectName(u"btn_newtask")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.btn_newtask.setFont(font3)
        self.btn_newtask.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.verticalLayout.addWidget(self.btn_newtask)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 368, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
#if QT_CONFIG(tooltip)
        self.tb_new_task_title.setToolTip(QCoreApplication.translate("MainWindow", u"Title", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tb_new_task_description.setToolTip(QCoreApplication.translate("MainWindow", u"description", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_priority.setToolTip(QCoreApplication.translate("MainWindow", u"If this task is important clicked", None))
#endif // QT_CONFIG(tooltip)
        self.cb_priority.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
#if QT_CONFIG(tooltip)
        self.btn_newtask.setToolTip(QCoreApplication.translate("MainWindow", u"add new task", None))
#endif // QT_CONFIG(tooltip)
        self.btn_newtask.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

