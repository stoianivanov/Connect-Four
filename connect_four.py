import copy
import random
import sys 

from PyQt5.QtCore import pyqtSignal, QBasicTimer, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)


class TableWindow(QWidget):
    def __init__(self):
        super(TableWindow, self).__init__()
        firstButton = QPushButton("&First")
        firstButton.setFocusPolicy(Qt.NoFocus)
        firstButton.clicked.connect(self.first_button_clicked)

        secondButton = QPushButton("&Second")
        secondButton.setFocusPolicy(Qt.NoFocus)

        thirdButton = QPushButton("&Third")
        thirdButton.setFocusPolicy(Qt.NoFocus)

        fourButton = QPushButton("&Four")
        fourButton.setFocusPolicy(Qt.NoFocus)

        fiveButton = QPushButton("&Five")
        fiveButton.setFocusPolicy(Qt.NoFocus)

        sixButton = QPushButton("&Six")
        sixButton.setFocusPolicy(Qt.NoFocus)

        layout = QGridLayout()
        layout.addWidget(firstButton, 0, 0)
        layout.addWidget(secondButton, 0, 1)
        layout.addWidget(thirdButton, 0, 2)
        layout.addWidget(fourButton, 0, 3)
        layout.addWidget(fiveButton, 0, 4)
        layout.addWidget(sixButton, 0, 5)

        self.setLayout(layout)

        self.setWindowTitle("Tetrix")
        self.resize(550, 370)

    def first_button_clicked(self):
        print("First button Clicked")


class Table:
    EMPTY = "E"
    RED = "R"
    BLACK = "B"

    def __init__(self):
        row = 10 * [self.EMPTY]
        self.matrix = []
        for i in range(0, 10):
            self.matrix.append(row)

    def col_is_full(self, col):
        for i in range(0, len(self.matrix)):
            if i[col] != "E":
                return False
        return True

    def get_matrix(self):
        return self.matrix

    def is_winner(self, player):
        pass

    def get_computer_turn(self):
        return random.randint(0, 11)

    def computer_turn(self):
        pos = self.get_computer_turn()
        while self.col_is_full(pos):
            pos = self.get_computer_turn()
        return pos

    def player_turn(self, pos):
        pass

    def commit_turn(self, pos):
        pass


if __name__ == '__main__':
    t = Table()
    print(t.get_matrix())
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec_())
