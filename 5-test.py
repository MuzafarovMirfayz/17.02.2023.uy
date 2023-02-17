from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vMainLay = QVBoxLayout()
        self.sana = 0
        self.sav1()
    
    def sav1(self):
        self.savol = QLabel("MYU - BAR kechagi hisob")

        self.v1 = QRadioButton("2-1")
        self.v2 = QRadioButton('2-2')
        self.v3 = QRadioButton('3-2')
        self.v4 = QRadioButton('1-3')
        self.checkBtn = QPushButton("Next")

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.checkBtn)
        

        self.setLayout(self.vMainLay)
        self.checkBtn.clicked.connect(self.sav2)


    def sav2(self):
        if self.v2.isChecked():
            self.sana += 1
        self.checkBtn.hide()
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.savol.hide()

        self.savol = QLabel("Arsenal - Manchester city")

        self.v1 = QRadioButton("2-1")
        self.v2 = QRadioButton('2-2')
        self.v3 = QRadioButton('3-2')
        self.v4 = QRadioButton('1-3')


        self.checkBtn = QPushButton("Next")

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.checkBtn)
        self.checkBtn.clicked.connect(self.sav3)


    def sav3(self):
        if self.v4.isChecked():
            self.sana += 1
        self.checkBtn.hide()
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.savol.hide()

        self.savol = QLabel("Real Madrid - Elche")

        self.v1 = QRadioButton("2-1")
        self.v2 = QRadioButton('2-2')
        self.v3 = QRadioButton('3-2')
        self.v4 = QRadioButton('4-0')
        self.checkBtn = QPushButton("Next")

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.checkBtn)
        self.checkBtn.clicked.connect(self.sav4)
        
    def sav4(self):
        if self.v4.isChecked():
            self.sana += 1
        self.checkBtn.hide()
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.savol.hide()
        self.savol = QLabel("Levandovskiy kecha nechta gol urdi")

        self.v1 = QRadioButton("1")
        self.v2 = QRadioButton('2')
        self.v3 = QRadioButton('0')
        self.v4 = QRadioButton('3')
        self.checkBtn = QPushButton("Next")

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.checkBtn)
        self.checkBtn.clicked.connect(self.sav5)
    
    def sav5(self):
        if self.v3.isChecked():
            self.sana += 1
        self.checkBtn.hide()
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.savol.hide()

        self.savol = QLabel("Reshford kecha nechta gol urdi")

        self.v1 = QRadioButton("1")
        self.v2 = QRadioButton('2')
        self.v3 = QRadioButton('0')
        self.v4 = QRadioButton('3')
        self.checkBtn = QPushButton("Next")

        self.vMainLay.addWidget(self.savol)
        self.vMainLay.addWidget(self.v1)
        self.vMainLay.addWidget(self.v2)
        self.vMainLay.addWidget(self.v3)
        self.vMainLay.addWidget(self.v4)
        self.vMainLay.addWidget(self.checkBtn)
        self.checkBtn.clicked.connect(self.tuga)

    def tuga(self):
        if self.v1.isChecked():
            self.sana+=1
        self.checkBtn.hide()
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.savol.hide()

        self.checkBtn.hide()
       
        self.savol = QLabel(f"{self.sana}-to'g'ri")
        self.vMainLay.addWidget(self.savol)
app = QApplication([])
obj = Window()
obj.show()
app.exec_()