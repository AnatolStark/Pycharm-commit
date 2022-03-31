import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Show Input', self)
        self.btn.move(250, 150)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter your age:', 18, 18, 65, 1)
        # if b_ok:
            # QMessageBox.information(self, 'Age', 'Your age is ' + str(i_age))
        # else:
            # QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')

        colors = ['red', 'orange', 'green', 'blue']
        s_color, b_ok = QInputDialog.getItem(self, 'Title', 'Enter your favorite color:', colors)
        if b_ok:
            QMessageBox.information(self, 'Color', 'Your favorite color is ' + s_color)
        else:
            QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
