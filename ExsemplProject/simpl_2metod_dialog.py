import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Show Message', self)
        self.btn.move(250, 150)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        msgDiskFull = QMessageBox()  #  dlja bolee sloshnyh widgetov
        msgDiskFull.setText('Yuor disk drive is almost full')
        msgDiskFull.setDetailedText('Please free up disk space')
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle('Full Drive')
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
