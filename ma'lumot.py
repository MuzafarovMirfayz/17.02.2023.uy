from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.vMainLay = QVBoxLayout()
        self.start()
    def start(self):
        self.lbl = QLabel()
        self.lbl.hide()
        self.com1 = QComboBox()
        self.com2 = QComboBox()
        self.com3 = QComboBox()
        self.com4 = QComboBox()
        self.com1.addItems(['','Andijon viloyati', 'Buxoro viloyati', 'Fargʻona viloyati', 'Jizzax viloyati', 'Xorazm viloyati', 'Namangan viloyati', 'Navoiy viloyati',
                            'Qashqadaryo viloyati', 'Samarqand viloyati', 'Sirdaryo viloyati', 'Surxondaryo viloyati', "Toshkent viloyati" ])
        self.com2.addItems(['','Andijon shahri', 'Buxoro shahri', 'Fargʻona shahri', 'Jizzax shahri', 'Xorazm shahri', 'Namangan shahri', 'Navoiy shahri',
                            'Qashqadaryo shahri', 'Samarqand shahri', 'Sirdaryo shahri', 'Surxondaryo shahri', "Toshkent shahri" ])        
        self.com2.hide()
        self.com3.addItems(['',"Erkak", "Ayol"])
        self.com3.hide()
        self.com4.addItems(['',"Rus", "O'zbek", "Tojik", "Qozoq"])
        self.com4.hide()
        self.com1.activated[str].connect(self.bir)
        self.com2.activated[str].connect(self.ikki)
        self.com3.activated[str].connect(self.uch)
        self.com4.activated[str].connect(self.yakun)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.com1)
        self.vMainLay.addWidget(self.com2)
        self.vMainLay.addWidget(self.com3)
        self.vMainLay.addWidget(self.com4)
        self.setLayout(self.vMainLay)
    def bir(self, text):
        self.a:str = text
        self.com2.show()
    def ikki(self, text):
        self.com3.show()
        self.a = self.a + "\n" + text
    def uch(self, text):
        self.com4.show()
        self.a = self.a + "\n" + text
    def yakun(self, text):
        self.com1.hide()
        self.com2.hide()
        self.com3.hide()
        self.com4.hide()
        self.a = self.a + "\n" + text
        self.lbl.setText(self.a)
        self.lbl.show()
app = QApplication([])
obj = window()
obj.show()
app.exec_()