import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QGridLayout,
        QLCDNumber, QPushButton, QWidget)

from PySide.QtCore import *
from PySide.QtGui import *

from connect_four import TableWindow, Table


class StartGame(QWidget):
    """
    Главния прозорец в играта.
    Предоставя възможност за игра срешу човек и игра срещу компютър.
    """
    def __init__(self):

        super(StartGame, self).__init__()
        self.table_window = TableWindow()
        onePlayerButton = QPushButton("&Single Player")
        onePlayerButton.setFocusPolicy(Qt.NoFocus)
        onePlayerButton.clicked.connect(self.start_single_player)

        multiPlayerButton = QPushButton("&Multi Player")
        multiPlayerButton.setFocusPolicy(Qt.NoFocus)
        multiPlayerButton.clicked.connect(self.start_multi_player)
        layout = QGridLayout()
        layout.addWidget(onePlayerButton, 0, 1)
        layout.addWidget(multiPlayerButton, 1, 1)
        self.setLayout(layout)

    def start_single_player(self):
        self.table_window.t.matrix = Table.MATRIX
        self.table_window.show()

    def start_multi_player(self):
        self.table_window.t.matrix = Table.MATRIX
        self.table_window.vsPC = False
        self.table_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartGame()
    window.show()
    sys.exit(app.exec_())
