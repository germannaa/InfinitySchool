

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit

#""Constante""
TAMANHO_FONTE = 25


layout = QVBoxLayout()
app = QApplication()
base = QWidget()
janela = QMainWindow()

font = QFont()
font.setPixelSize(TAMANHO_FONTE)

label = QLabel('Infinity School')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)


label2 = QLabel('Login')
label2.setFont(font)
label2.setAlignment(Qt.AlignCenter)

txt_login = QLineEdit()

label3 = QLabel('Senha')
label2.setFont(font)
label2.setAlignment(Qt.AlignCenter)

txt_senha = QLineEdit()

botao = QPushButton('Botão')
botao.setFont(font)


layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(txt_login)
layout.addWidget(label3)
layout.addWidget(txt_senha)
layout.addWidget(botao)

base.setLayout(layout)
janela.setCentralWidget(base)

janela.show()
app.exec()
