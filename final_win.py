from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.v_line = QVBoxLayout()
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.v_line.addWidget(self.txt_index, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
    def results(self):
        pass
