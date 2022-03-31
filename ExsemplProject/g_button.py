import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Disable Label', self)
        self.btn.setIcon(QIcon(QPixmap('pictures/img.png')))
        self.btn.setFlat(False)
        self.btn.move(250, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(265, 100)
        self.lbl.resize(297, 279)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        if self.lbl.isEnabled(): #  dostupnyi
            self.lbl.setDisabled(True)  #  nedostupnyi
            self.btn.setText('Enable Label')
        else:
            self.lbl.setEnabled(True)
            self.btn.setText('Disable Label')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
