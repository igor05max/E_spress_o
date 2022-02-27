import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffee_table = self.coffee_table
        con = sqlite3.connect("coffee.sqlite3")
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        self.coffee_table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j in range(len(row)):
                el = str(row[j])
                item = QTableWidgetItem(el)
                self.coffee_table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
