#Instalar package PyQt5, mysql-connector
from PyQt5 import uic, QtWidgets

# ------- ("BACK") -------

def cadastro():
    print("Teste")









#------- INICIO ------- ("FRONT")
#Gerar a Aplicacao

app = QtWidgets.QApplication([])

#Carreqar o arquivo .ui

formulario = uic.loadUi('login.ui')

#Acao do botao
formulario.pushButton.clicked.connect(cadastro)

#Exibir tela
formulario.show()
app.exec()
