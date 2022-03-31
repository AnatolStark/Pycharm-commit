import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.cmbState = QComboBox(self)
        self.cmbState.move(50, 50)
        # self.cmbState.addItems(['AL', 'AR', 'MA', 'MO', 'MI'])
        self.cmbState.addItem('Alabama', 'AL')
        self.cmbState.addItem('Alaska', 'AS')
        self.cmbState.addItem('Minnesota', 'MA')
        self.cmbState.addItem('Missouri', 'MO')
        self.cmbState.addItem('Michigan', 'MI')
        self.cmbState.currentIndexChanged.connect(self.evt_cmb_state_changed)
        self.cmbState.highlighted.connect(self.evt_cmb_state_highLighted)

        self.lblAbbr = QLabel('State Abbreviation: AL', self)
        self.lblAbbr.resize(150, 30)
        self.lblAbbr.move(180, 50)

        # redaktiruemyi ComboBox

        self.cmbPosts = QComboBox(self)
        self.cmbPosts.move(50, 90)
        self.cmbPosts.resize(200, 50)
        self.cmbPosts.setEditable(True)
        self.cmbPosts.setDuplicatesEnabled(False)
        self.cmbPosts.addItem('First Post', 'asdgfjüp')
        self.cmbPosts.addItem('Second Post', 'lojiuuggf')
        self.cmbPosts.addItem('Third Post', 'iuhzr456')
        self.cmbPosts.currentIndexChanged.connect(self.evt_cmb_posts_changed)

    def evt_cmb_posts_changed(self, idx):
        if not self.cmbPosts.itemData(idx):
            input_str, bool_ok = QInputDialog.getText(self, 'Your Nickname', 'Enter your nickname for "{}"'
                                                      .format(self.cmbPosts.itemText(idx)))
            if bool_ok:
                self.cmbPosts.setItemData(idx, input_str)
        QMessageBox.information(self, 'Posts', 'You have selected "{}"'. format(self.cmbPosts.itemData(idx)))


    def evt_cmb_state_changed(self, idx):
        QMessageBox.information(self, 'ComboBox', 'You have selected {}'.format(self.cmbState.itemData(idx)))

    def evt_cmb_state_highLighted(self, idx):
        self.lblAbbr.setText('State Abbreviation: {}'.format(self.cmbState.itemData(idx)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
