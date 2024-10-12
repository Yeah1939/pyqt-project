from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox
app = QApplication([])
win = QWidget()
win.resize(400,300)
win.setWindowTitle('конкурс')

question = QLabel('В якому році канал отримав золоту кнопку від YouTube?')
a1 = QRadioButton('2005')
a2 = QRadioButton('2010')
a3 = QRadioButton('2015')
a4 = QRadioButton('2020')

layout1 = QHBoxLayout()
layout1.addWidget(a1, alignment=Qt.AlignCenter)
layout1.addWidget(a2, alignment=Qt.AlignCenter)

layout2 = QHBoxLayout()
layout2.addWidget(a3, alignment=Qt.AlignCenter)
layout2.addWidget(a4, alignment=Qt.AlignCenter)

main_layout = QVBoxLayout()
main_layout.addWidget(question)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)

win.setLayout(main_layout)

def winner():
    qm = QMessageBox()
    qm.setText('You win')
    qm.exec_()

def lose():
    qm = QMessageBox()
    qm.setText('You lose')
    qm.exec_()

a1.clicked.connect(lose)
a2.clicked.connect(winner)
a3.clicked.connect(lose)
a4.clicked.connect(lose)

win.show()
app.exec_()
