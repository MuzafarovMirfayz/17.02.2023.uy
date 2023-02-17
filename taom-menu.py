from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox
try:
    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.vMain = QVBoxLayout()
            self.gor1 = QHBoxLayout()
            self.gor2 = QHBoxLayout()
            self.gor3 = QHBoxLayout()
            self.gor4 = QHBoxLayout()
            self.gor5 = QHBoxLayout()
            self.gor6= QHBoxLayout()


            self.menu()

        def menu(self):


            self.umumiy = QLabel() 
            self.umumiy.hide()

            self.bolim = QLabel("Quyuq")
            self.bolim1 = QLabel('Suyuq')
            self.bolim2 = QLabel("Ichimlik")
            self.gor1.addWidget(self.bolim)
            self.gor1.addWidget(self.bolim1)
            self.gor1.addWidget(self.bolim2)

            self.suy1 = QCheckBox("Mastava")
            self.quy1 = QCheckBox("Osh")
            self.ich1 = QCheckBox("Coca-cola")
            self.gor2.addWidget(self.suy1)
            self.gor2.addWidget(self.quy1)
            self.gor2.addWidget(self.ich1)

            self.suy2 = QCheckBox("Sho'rva")
            self.quy2 = QCheckBox("Tovuq")
            self.ich2 = QCheckBox("Choy")
            self.gor3.addWidget(self.suy2)
            self.gor3.addWidget(self.quy2)
            self.gor3.addWidget(self.ich2)

            self.suy3 = QCheckBox("Borsh")
            self.quy3 = QCheckBox("Jiz")
            self.ich3 = QCheckBox("Cofe")
            self.gor4.addWidget(self.suy3)
            self.gor4.addWidget(self.quy3)
            self.gor4.addWidget(self.ich3)

            self.suy4 = QCheckBox("Tovuq shorva")
            self.quy4 = QCheckBox("Sushi")
            self.ich4 = QCheckBox("Fanta")
            self.gor5.addWidget(self.suy4)
            self.gor5.addWidget(self.quy4)
            self.gor5.addWidget(self.ich4)

            self.suy5 = QCheckBox("Tom Yam sho'rvasi")
            self.quy5 = QCheckBox("Lazanya")
            self.ich5 = QCheckBox("Pepsi")
            self.gor6.addWidget(self.suy5)
            self.gor6.addWidget(self.quy5)
            self.gor6.addWidget(self.ich5)

            self.hibutn = QPushButton("Chek")
            self.hibutn.clicked.connect(self.hisob)

            self.tab = {self.suy1:15000, self.suy2:16000, self.suy3:15000, self.suy4:20000, self.suy5:25000, 
                   self.quy1:18000, self.quy2:32000, self.quy3:50000, self.quy4:50000, self.quy5:30000,
                   self.ich1:11000, self.ich2:3000, self.ich3:5000, self.ich4:11000, self.ich5:11000}

            self.vMain.addLayout(self.gor1)
            self.vMain.addLayout(self.gor2)
            self.vMain.addLayout(self.gor3)
            self.vMain.addLayout(self.gor4)
            self.vMain.addLayout(self.gor5)
            self.vMain.addWidget(self.hibutn)

            self.setLayout(self.vMain)

        def hisob(self):
            self.a = ""
            self.pul = 0
            for i in self.tab:
                i.hide()
            for i in self.tab:
                if i.isChecked():
                    self.pul += self.tab[i]
                    self.a = self.a + "\n" + f"{i.text()}-{self.tab[i]}" 
            self.a = self.a + "\n" + f"Umumiy hisob -> {self.pul}" 

            self.bolim.hide()
            self.bolim1.hide()
            self.bolim2.hide()
            self.hibutn.setText("Back")
            self.hibutn.clicked.connect(self.back)
            self.bolim2.setText(self.a)
            self.bolim2.show()

        def back(self):
            self.bolim2.hide()
            self.hibutn.hide()
            self.menu()
except:
    pass
app = QApplication([])
obj = Window()
obj.show()
app.exec_()
