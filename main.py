from PyQt5 import uic
from PyQt5.QtGui import QFont
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
import sys


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_table()

    def load_table(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute('''SELECT * from coffees''').fetchall()
        font = QFont()
        font.setPointSize(10)
        self.headers = ["id", "grade", "degree of roast", "grounded/in grains", "description", "cost", "volume"]
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())