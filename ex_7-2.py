import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Original',self)
        btn3 = QPushButton('Small', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeOriginal)
        btn3.clicked.connect(self.resizeSmall)


        self.setWindowTitle('보일러')
        self.setGeometry(300, 300, 300, 400)
        self.show()
###############################################################
    # def setDial(self):
    #     # Dial의 최대/최솟값과 PageStep/SingleStep값을 변경합니다.
    #     self.setMaximum(500)
    #     self.setMinimum(-500)
    #     self.setPageStep(100)
    #     self.setSingleStep(20)
##############################################################
    def resizeBig(self):
        self.resize(600, 800)

    def resizeOriginal(self):
        self.resize(300,400)

    def resizeSmall(self):
        self.resize(150, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())