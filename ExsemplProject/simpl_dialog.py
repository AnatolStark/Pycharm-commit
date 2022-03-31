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

         #  staticheskij metod - result = QMessageBox...(parent,'Title', Message'

        # res = QMessageBox.information(self, 'Disk Full', 'Yuor disk drive is almost full')
        # res = QMessageBox.warning(self, 'Disk Full', 'Yuor disk drive is almost full')
        # res = QMessageBox.critical(self, 'Disk Full', 'Yuor disk drive is almost full')
        # res = QMessageBox.question(self, 'Disk Full', 'Yuor disk drive is almost full')
        # print((res))
        res = QMessageBox.question(self, 'Disk Full', 'Yuor disk drive is almost full')
        if res == QMessageBox.Yes:
            QMessageBox.information(self, '', "You've clicked 'Yes' button")
        elif res == QMessageBox.No:
            QMessageBox.information(self, '', "You've clicked 'No' button")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())