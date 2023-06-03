from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from instr import *
from second_win import *

class MainWin(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    
    def set_appear(self):
        self.setWindowTitle(txt_titel)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
  
    
    def initUI(self):
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()

        self.layout.addWidget(
            txt_hello, alignment = Qt.AlignLeft
        )
        self.layout.addWidget(
            txt_instruction, alignment = Qt.AlignLeft
        )
        self.layout.addWidget(
            txt_next, alignment = Qt.AlignCenter
        )
        self.setLayout(layout)

    
    def connects(self):
        self.txt_next.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = TestWin()





app = QApplication([])
main_win = QWidget()
app.exec_()