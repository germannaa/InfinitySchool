
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow

#""Constante""
TAMANHO_FONTE = 30


layout = QVBoxLayout()
app = QApplication()
base = QWidget()
janela = QMainWindow()

font = QFont()
font.setPixelSize(TAMANHO_FONTE)

label = QLabel('Infinity School')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)

botao = QPushButton('Botão')
botao.setFont(font)

layout.addWidget(label)
layout.addWidget(botao)

base.setLayout(layout)
janela.setCentralWidget(base)

janela.show()
app.exec()
