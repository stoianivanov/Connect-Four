from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)

from PySide.QtCore import *
from PySide.QtGui import *


class ComputerWinDialog(QWidget):
    """
    Стартира се когато компютъра спечели.
    """
    def __init__(self):

        super(ComputerWinDialog, self).__init__()
        self.label = QLabel()
        text = "Computer WIN"
        self.label.setText(text)
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 1)
        self.setLayout(layout)
