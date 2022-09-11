
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit

#""Constante""
TAMANHO_FONTE = 20


layout = QVBoxLayout()
app = QApplication()
base = QWidget()
janela = QMainWindow()

font = QFont()
font.setPixelSize(TAMANHO_FONTE)

label = QLabel('Infinity School')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)


lbl_login = QLabel('Login')
txt_login = QLineEdit()

lbl_senha = QLabel('Senha')
txt_senha = QLineEdit()
txt_senha.setEchoMode(QLineEdit.Password)
#Ctrl espaco
#Alt enter


botao = QPushButton('Entrar')


layout.addWidget(label)
layout.addWidget(lbl_login)
layout.addWidget(txt_login)
layout.addWidget(lbl_senha)
layout.addWidget(txt_senha)
layout.addWidget(botao)

base.setLayout(layout)
janela.setCentralWidget(base)

janela.show()
app.exec()
