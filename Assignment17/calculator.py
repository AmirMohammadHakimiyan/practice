import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
my_app=QApplication([])
loader=QUiLoader()
my_window=loader.load("calcu.ui")
def sum():         #جمع
    global amell
    amell="+"
    number=my_window.lineEdit.text()
    number+="+"
    my_window.lineEdit.setText(number)
def sub():      #منها
    global amell
    amell="-"
    number=my_window.lineEdit.text()
    number+="-"
    my_window.lineEdit.setText(number)
def multi():       #ضرب
    global amell
    amell="*"
    number=my_window.lineEdit.text()
    number+="*"
    my_window.lineEdit.setText(number)
def division():     #تقسیم
    global amell
    amell="/"
    number=my_window.lineEdit.text()
    number+="/"
    my_window.lineEdit.setText(number)
def sin():
    global amell
    amell="sin"
    number=my_window.lineEdit.text()
    number2=math.sin(int(number))
    my_window.lineEdit.setText(str(number2))
def cos():
    global amell
    amell="cos"
    number=my_window.lineEdit.text()
    number2=math.cos(int(number))
    my_window.lineEdit.setText(str(number2))
def tan():
    global amell
    amell="tan"
    number=my_window.lineEdit.text()
    number2=math.tan(int(number))
    my_window.lineEdit.setText(str(number2))
def cot():
    global amell
    amell="cot"
    number=my_window.lineEdit.text()
    number2=math.cot(int(number))
    my_window.lineEdit.setText(str(number2))
def log():
    global amell
    amell="log"
    number=my_window.lineEdit.text()
    number2=math.log(int(number))
    my_window.lineEdit.setText(str(number2))
def c():
    my_window.lineEdit.setText("")
def equal():        #مساوی
    if amell=="+":
        answer=my_window.lineEdit.text().split("+")
        c=0
        for i in answer:
            c+=int(i)
        my_window.lineEdit.setText(str(c))
    elif amell=="-":
        answer=my_window.lineEdit.text().split("-")
        c=int(answer[0])
        c-=int(answer[1])
        my_window.lineEdit.setText(str(c))
    elif amell=="*":
        answer=my_window.lineEdit.text().split("*")
        c=int(answer[0])
        c*=int(answer[1])
        my_window.lineEdit.setText(str(c))
    elif amell=="/":
        answer=my_window.lineEdit.text().split("/")
        c=int(answer[0])
        c//=int(answer[1])
        my_window.lineEdit.setText(str(c))
def writ1():
    m=my_window.lineEdit.text()
    m+=str(1)
    my_window.lineEdit.setText(m)
def writ2():
    m=my_window.lineEdit.text()
    m+=str(2)
    my_window.lineEdit.setText(m)
def writ3():
    m=my_window.lineEdit.text()
    m+=str(3)
    my_window.lineEdit.setText(m)
def writ4():
    m=my_window.lineEdit.text()
    m+=str(4)
    my_window.lineEdit.setText(m)
def writ5():
    m=my_window.lineEdit.text()
    m+=str(5)
    my_window.lineEdit.setText(m)
def writ6():
    m=my_window.lineEdit.text()
    m+=str(6)
    my_window.lineEdit.setText(m)
def writ7():
    m=my_window.lineEdit.text()
    m+=str(7)
    my_window.lineEdit.setText(m)
def writ8():
    m=my_window.lineEdit.text()
    m+=str(8)
    my_window.lineEdit.setText(m)
def writ9():
    m=my_window.lineEdit.text()
    m+=str(9)
    my_window.lineEdit.setText(m)
def writ0():
    m=my_window.lineEdit.text()
    m+=str(0)
    my_window.lineEdit.setText(m)
my_window.pu1.clicked.connect(writ1)
my_window.pu2.clicked.connect(writ2)
my_window.pu3.clicked.connect(writ3)
my_window.pu4.clicked.connect(writ4)
my_window.pu5.clicked.connect(writ5)
my_window.pu6.clicked.connect(writ6)
my_window.pu7.clicked.connect(writ7)
my_window.pu8.clicked.connect(writ8)
my_window.pu9.clicked.connect(writ9)
my_window.pu0.clicked.connect(writ0)
my_window.pusum.clicked.connect(sum)
my_window.puequal.clicked.connect(equal)
my_window.pusub.clicked.connect(sub)
my_window.pumulti.clicked.connect(multi)
my_window.pudivi.clicked.connect(division)
my_window.pusin.clicked.connect(sin)
my_window.pucos.clicked.connect(cos)
my_window.putan.clicked.connect(tan)
my_window.pucot.clicked.connect(cot)
my_window.pulog.clicked.connect(log)
my_window.puc.clicked.connect(c)
my_window.show()
my_app.exec()