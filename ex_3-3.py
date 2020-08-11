import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


def MyMenu():
    print('Please select the menu')

class MyApp(QWidget):

    def __init__(self):
      super().__init__()
      self.initUI()


    def initUI(self):

        btn1 = QPushButton('Quit', self)
        btn1.move(700, 450)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)

        btn2 = QPushButton("Can I take your order?", self)
        btn2.move(330, 190)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(MyMenu)

        self.setWindowTitle('Burger KING')
        #self.setGeometry(300, 300, 800, 500)
        self.resize(800, 500)
        self.center()
        self.show()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('burger_king_PNG4.png'))

    def center(self):
         qr = self.frameGeometry()
         cp = QDesktopWidget().availableGeometry().center()
         qr.moveCenter(cp)
         self.move(qr.topLeft())
       #self.setGeometry(300, 300, 300, 200)
       #self.show()


#################################################################
# class MeNu(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

    # def initUI(self):
        # btn1 = QPushButton('Cheese Burger', self)
        # btn1.move(50, 20)
        # btn1.resize(btn1.sizeHint())
        # btn1.clicked.connet(int(input('주문 수량')))

        # btn2 = QPushButton('Wapper',self)
        # btn2.move(50,30)
        # btn2.resize(btn2.sizeHint())
        # btn2.clicked.connect(int(input('주문 수량')))

        # btn3 = QPushButton('Wapper Jr.', self)
        # btn3.move(50, 50)
        # btn3.resize(btn3.sizeHint())
        # btn3.clicked.connect(int(input('주문 수량')))

        # btn4 = QPushButton('Cheese Wapper', self)
        # btn4.move(50, 70)
        # btn4.resize(btn2.sizeHint())
        # btn4.clicked.connect(int(input('주문 수량')))

        # self.setGeometry(300, 300, 300, 200)
        # self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())