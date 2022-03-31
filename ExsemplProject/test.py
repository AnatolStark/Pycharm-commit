import sys
from PyQt5.QtWidgets import *  #  sekzija importov

# app = QApplication(sys.argv)  #  sozdaem priloshenija
# dlgMain = QWidget()           #  sozdaem glavnoe okno window
# dlgMain = QDialog()     # imeet dopolnitelnye svoistva i metody, chem QWidget
# dlgMain = QMainWindow()   # menshe okno, no bolshe vozmoshnoctei
# dlgMain.setWindowTitle('First GUI')   # ustanavlivaem svoistva okna, wigety
# dlgMain.show()                #  pokazyvaem okno GUI


class DlgMain(QDialog):
    def __init__(self):  # __init__ - Funkzija opredeljaetsja vnutri klassa
        super().__init__()         #  byzyvaem klass roditelja
        self.setWindowTitle('Second GUI')  #  dobavljaem widget i svoistva
        self.resize(600, 300)  #  rasmery okna

        self.ledText = QLineEdit('Default Text', self)  #  vvodit text
        self.ledText.move(200, 50)  #  sdvigaet widget

        self.btnUpdate = QPushButton('Update Window Title', self)  #  self - ukasyvaet gde nachoditsja widget
        self.btnUpdate.move(200, 80)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)  #  obrabotka sobytij


    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())

if __name__ == '__main__':         #  __name__ - proverjaet importiruemyi modul ili eto drugaja programma
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())                  # zapuskaem priloshenie