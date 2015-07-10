import copy
import random
import sys

from turn import ComputerTurn, Turn, HummanTurn
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)

from PySide.QtCore import *
from PySide.QtGui import *

from win_dialog import *
from table import Table
from computer import Computer


class TableWindow(QWidget):
    def __init__(self):

        super(TableWindow, self).__init__()
        self.cols = []
        self.pc = Computer("B")
        self.vsPC = True
        self.win_dialog = WinDialog()
        self.col_one_edit = QTextEdit()
        self.col_one_edit.setReadOnly(True)

        self.col_two_edit = QTextEdit()
        self.col_two_edit.setReadOnly(True)

        self.col_three_edit = QTextEdit()
        self.col_three_edit.setReadOnly(True)

        self.col_four_edit = QTextEdit()
        self.col_four_edit.setReadOnly(True)

        self.col_five_edit = QTextEdit()
        self.col_five_edit.setReadOnly(True)

        self.col_six_edit = QTextEdit()
        self.col_six_edit.setReadOnly(True)

        self.col_seven_edit = QTextEdit()
        self.col_seven_edit.setReadOnly(True)

        self.col_eight_edit = QTextEdit()
        self.col_eight_edit.setReadOnly(True)

        self.col_nine_edit = QTextEdit()
        self.col_nine_edit.setReadOnly(True)

        self.col_ten_edit = QTextEdit()
        self.col_ten_edit.setReadOnly(True)

        self.col_one_edit = QTextEdit()
        self.col_one_edit.setReadOnly(True)

        label_on_turn = QLabel()
        label_on_turn.setText("On turn:")

        self.player = QLabel()
        self.player.setText("R")

        self.adding_to_vector()
        self.onTurn = 1
        self.t = Table()

        self.read_table()

        firstButton = QPushButton("&")
        firstButton.setFocusPolicy(Qt.NoFocus)
        firstButton.clicked.connect(self.first_button_clicked)

        secondButton = QPushButton("&")
        secondButton.setFocusPolicy(Qt.NoFocus)
        secondButton.clicked.connect(self.second_button_clicked)

        thirdButton = QPushButton("&")
        thirdButton.setFocusPolicy(Qt.NoFocus)
        thirdButton.clicked.connect(self.third_button_clicked)

        fourButton = QPushButton("&")
        fourButton.setFocusPolicy(Qt.NoFocus)
        fourButton.clicked.connect(self.four_button_clicked)

        fiveButton = QPushButton("&")
        fiveButton.setFocusPolicy(Qt.NoFocus)
        fiveButton.clicked.connect(self.five_button_clicked)

        sixButton = QPushButton("&")
        sixButton.setFocusPolicy(Qt.NoFocus)
        sixButton.clicked.connect(self.six_button_clicked)

        sevenButton = QPushButton("&")
        sevenButton.setFocusPolicy(Qt.NoFocus)
        sevenButton.clicked.connect(self.seven_button_clicked)

        eigthButton = QPushButton("&")
        eigthButton.setFocusPolicy(Qt.NoFocus)
        eigthButton.clicked.connect(self.eigth_button_clicked)

        nineButton = QPushButton("&")
        nineButton.setFocusPolicy(Qt.NoFocus)
        nineButton.clicked.connect(self.nine_button_clicked)

        tenButton = QPushButton("&")
        tenButton.setFocusPolicy(Qt.NoFocus)
        tenButton.clicked.connect(self.ten_button_clicked)

        layout = QGridLayout()
        layout.addWidget(firstButton, 0, 0)
        layout.addWidget(secondButton, 0, 1)
        layout.addWidget(thirdButton, 0, 2)
        layout.addWidget(fourButton, 0, 3)
        layout.addWidget(fiveButton, 0, 4)
        layout.addWidget(sixButton, 0, 5)
        layout.addWidget(sevenButton, 0, 6)
        layout.addWidget(eigthButton, 0, 7)
        layout.addWidget(nineButton, 0, 8)
        layout.addWidget(tenButton, 0, 9)
        layout.addWidget(self.col_one_edit, 1, 0)
        layout.addWidget(self.col_two_edit, 1, 1)
        layout.addWidget(self.col_three_edit, 1, 2)
        layout.addWidget(self.col_four_edit, 1, 3)
        layout.addWidget(self.col_five_edit, 1, 4)
        layout.addWidget(self.col_six_edit, 1, 5)
        layout.addWidget(self.col_seven_edit, 1, 6)
        layout.addWidget(self.col_eight_edit, 1, 7)
        layout.addWidget(self.col_nine_edit, 1, 8)
        layout.addWidget(self.col_ten_edit, 1, 9)
        layout.addWidget(label_on_turn, 2, 0)
        layout.addWidget(self.player, 2, 1)

        self.setLayout(layout)

        self.setWindowTitle("Connect Four")
        self.resize(550, 450)

    def adding_to_vector(self):
        self.cols.append(self.col_one_edit)
        self.cols.append(self.col_two_edit)
        self.cols.append(self.col_three_edit)
        self.cols.append(self.col_four_edit)
        self.cols.append(self.col_five_edit)
        self.cols.append(self.col_six_edit)
        self.cols.append(self.col_seven_edit)
        self.cols.append(self.col_eight_edit)
        self.cols.append(self.col_nine_edit)
        self.cols.append(self.col_ten_edit)

    def read_table(self):
        result = ""
        i = 0
        for col in self.cols:
            for j in range(0, len(self.t.matrix)):
                result += self.t.matrix[j][i] + "\n-\n"
            i += 1
            col.setText(result)
            result = ""
        if self.t.has_winner():
            self.win_dialog.show()

    def first_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(0, "R")

            if self.vsPC:
                pos = self.pc.get_turn(self.t.matrix)
                print(pos)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                self.t.commit_turn(pos, "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(0, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def second_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(1, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(1, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def third_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(2, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(2, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def four_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(3, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(3, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def five_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(4, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(4, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def six_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(5, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(5, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def seven_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(6, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(6, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def eigth_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(7, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(7, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def nine_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(8, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(8, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

    def ten_button_clicked(self):
        if self.onTurn == 1:
            self.t.commit_turn(9, "R")
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(9, "B")
            self.player.setText("R")
            self.onTurn = 1
        self.read_table()

if __name__ == '__main__':
    t = Table()
    app = QApplication(sys.argv)
    window = TableWindow()
    p = window.palette()
    p.setColor(window.backgroundRole(), Qt.red)
    window.setPalette(p)
    window.show()
    sys.exit(app.exec_())
