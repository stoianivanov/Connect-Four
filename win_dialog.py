from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)

from PySide.QtCore import *
from PySide.QtGui import *


class WinDialog(QWidget):
    """
    Стартира се когато някой спечели.
    """
    def __init__(self):

        super(WinDialog, self).__init__()
        self.label = QTextEdit()
        text = "YOU WIN"
        self.label.setText(text)
        self.label.setTextColor(Qt.red)
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 1)
        self.setLayout(layout)
