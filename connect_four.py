import copy
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)

from PySide.QtCore import *
from PySide.QtGui import *

from win_dialog import WinDialog
from computer_win_dialog import ComputerWinDialog
from table import Table
from computer import Computer
from timer import Timer


class TableWindow(QWidget):
    """
    Визуализира играта.
    """
    def __init__(self):

        super(TableWindow, self).__init__()
        self.cols = []
        self.pc = Computer("B")
        self.vsPC = True
        self.win_dialog = WinDialog()
        self.compuret_win = ComputerWinDialog()

        self.first_player_time = Timer()
        self.first_player_time.start()

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

        self.player_time = QLabel()
        self.player_time.setText("Time player R:")

        self.player_game_time = QLabel()
        self.player_game_time.setText(" ")

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

        fourthButton = QPushButton("&")
        fourthButton.setFocusPolicy(Qt.NoFocus)
        fourthButton.clicked.connect(self.fourth_button_clicked)

        fifthButton = QPushButton("&")
        fifthButton.setFocusPolicy(Qt.NoFocus)
        fifthButton.clicked.connect(self.fifth_button_clicked)

        sixthButton = QPushButton("&")
        sixthButton.setFocusPolicy(Qt.NoFocus)
        sixthButton.clicked.connect(self.sixth_button_clicked)

        seventhButton = QPushButton("&")
        seventhButton.setFocusPolicy(Qt.NoFocus)
        seventhButton.clicked.connect(self.seventh_button_clicked)

        eighthButton = QPushButton("&")
        eighthButton.setFocusPolicy(Qt.NoFocus)
        eighthButton.clicked.connect(self.eighth_button_clicked)

        ninthButton = QPushButton("&")
        ninthButton.setFocusPolicy(Qt.NoFocus)
        ninthButton.clicked.connect(self.ninth_button_clicked)

        tenthButton = QPushButton("&")
        tenthButton.setFocusPolicy(Qt.NoFocus)
        tenthButton.clicked.connect(self.tenth_button_clicked)

        layout = QGridLayout()
        layout.addWidget(firstButton, 0, 0)
        layout.addWidget(secondButton, 0, 1)
        layout.addWidget(thirdButton, 0, 2)
        layout.addWidget(fourthButton, 0, 3)
        layout.addWidget(fifthButton, 0, 4)
        layout.addWidget(sixthButton, 0, 5)
        layout.addWidget(seventhButton, 0, 6)
        layout.addWidget(eighthButton, 0, 7)
        layout.addWidget(ninthButton, 0, 8)
        layout.addWidget(tenthButton, 0, 9)
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
        layout.addWidget(self.player_time, 2, 2)
        layout.addWidget(self.player_game_time, 2, 3)

        self.setLayout(layout)

        self.setWindowTitle("Connect Four")
        self.resize(550, 450)

    def adding_to_vector(self):
        """Добавя бутоните към масив от позициите
        на който може да се постави елемента"""
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
        """Прочита таблицата от Table и я попълва в UI-a.
        Ако има победител, пуска нов прозер.
        """
        result = ""
        i = 0
        for col in self.cols:
            for j in range(0, len(self.t.matrix)):
                result += self.t.matrix[j][i] + "\n-\n"
            i += 1
            col.setText(result)
            result = ""
        if self.t.has_winner():
            if self.t.get_winner() == Table.RED:
                print(self.first_player_time.stop())
                self.player_game_time.setText(str(self.first_player_time.stop()))
                self.win_dialog.show()
            else:
                self.compuret_win.show()

    def first_button_clicked(self):
        """Метод, който се извиква при натискането на първия бутон.
        Извършва ход в играта на позиция 0.
        """
        if self.onTurn == 1:
            self.t.commit_turn(0, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                pos = self.pc.get_turn(self.t.matrix)
                self.t.commit_turn(pos, "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(0, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def second_button_clicked(self):
        """Метод, който се извиква при натискането на втория бутон.
        Извършва ход в играта на позиция 1.
        """
        if self.onTurn == 1:
            self.t.commit_turn(1, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(1, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def third_button_clicked(self):
        """Метод, който се извиква при натискането на третия бутон.
        Извършва ход в играта на позиция 2.
        """
        if self.onTurn == 1:
            self.t.commit_turn(2, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(2, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def fourth_button_clicked(self):
        """Метод, който се извиква при натискането на четвътия бутон.
        Извършва ход в играта на позиция 3.
        """
        if self.onTurn == 1:
            self.t.commit_turn(3, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(3, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def fifth_button_clicked(self):
        """Метод, който се извиква при натискането на петия бутон.
        Извършва ход в играта на позиция 4.
        """
        if self.onTurn == 1:
            self.t.commit_turn(4, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(4, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def sixth_button_clicked(self):
        """Метод, който се извиква при натискането на шестия бутон.
        Извършва ход в играта на позиция 5.
        """
        if self.onTurn == 1:
            self.t.commit_turn(5, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(5, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def seventh_button_clicked(self):
        """Метод, който се извиква при натискането на седмия бутон.
        Извършва ход в играта на позиция 6.
        """
        if self.onTurn == 1:
            self.t.commit_turn(6, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(6, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def eighth_button_clicked(self):
        """Метод, който се извиква при натискането на осмият бутон.
        Извършва ход в играта на позиция 7.
        """
        if self.onTurn == 1:
            self.t.commit_turn(7, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(7, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def ninth_button_clicked(self):
        """Метод, който се извиква при натискането на деветия бутон.
        Извършва ход в играта на позиция 8.
        """
        if self.onTurn == 1:
            self.t.commit_turn(8, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(8, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
        self.read_table()

    def tenth_button_clicked(self):
        """Метод, който се извиква при натискането на десетия бутон.
        Извършва ход в играта на позиция 9.
        """
        if self.onTurn == 1:
            self.t.commit_turn(9, "R")
            self.first_player_time.sleep()
            if self.vsPC:
                self.t.commit_turn(self.pc.get_turn(
                    self.t.matrix), "B")
                self.first_player_time.start()
            else:
                self.onTurn = 2
                self.player.setText("B")
        else:
            self.t.commit_turn(9, "B")
            self.player.setText("R")
            self.onTurn = 1
            self.first_player_time.start()
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
