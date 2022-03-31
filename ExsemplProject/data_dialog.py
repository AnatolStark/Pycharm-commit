import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Dates', self)
        self.btn.move(250, 150)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt.toString())  #  Sa Mrz 19 2022
        print(dt.toJulianDay())  #2459658
        print(dt.dayOfWeek())  # 6
        print(dt.dayOfYear())   #  78
        print(dt.addDays(21).toString())  #  Sa Apr 9 2022

        tm1 = QTime(13, 20, 25, 346)
        tm2 = QTime(15, 20, 25, 346)
        tm = tm2.addSecs(60)
        print(tm1.toString())  #  13:20:25
        print(tm.toString())   #  15:21:25
        print(tm1.msec())  #  346
        print(tm1.secsTo(tm2))  #  7200

        dtm = QDateTime.currentDateTime()
        print(dtm.toString())    #Mo Mrz 21 14:58:50 2022


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())