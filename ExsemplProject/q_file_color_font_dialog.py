import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  #  dlja QColorDialog


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Show Input', self)
        self.btn.move(250, 150)
        font = QFont('Arial', 14, 75, True)   #     dlja   QColorDialog
        self.btn.setFont(font)     #     dlja   QColorDialog
        self.btn.clicked.connect(self.evt_btn_clicked)

    # def evt_btn_clicked(self):
        # res = QFileDialog.getOpenFileName(self, 'Open File', '/Usaers/Anatol', 'JPG File (*.jpg);;PNG File (*.png)')
        # print(res)

    # QColorDialog


    # def evt_btn_clicked(self):
        # color = QColorDialog.getColor(QColor('red'), self, 'Choose Color')
        # color = QColorDialog.getColor(QColor('#00ff00'), self, 'Choose Color')
        # color = QColorDialog.getColor(QColor(255, 0, 165, 255), self, 'Choose Color')   #  4 zifra - prosrachnost
        # print(color)

        #   QFontDialog

    def evt_btn_clicked(self):
        font, b_ok = QFontDialog.getFont()
        print(font, b_ok)
        if b_ok:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn.setFont(font)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
