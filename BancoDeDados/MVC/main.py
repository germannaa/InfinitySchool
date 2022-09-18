#Instalar package PyQt5, mysql-connector
from PyQt5 import uic, QtWidgets
import mysql.connector

#Banco

banco = mysql.connector.connect(
    host = "localhost",
    user = "germana",
    passwd = "123",
    database = "funcionario"
    #porta
)


# ------- ("BACK") -------

def cadastro():
    linhaLogin = formulario.lineEdit.text()
    linhaSenha = formulario.lineEdit_2.text()

    cursor = banco.cursor()
    comandoSQL = f'INSERT INTO usuario (nome, senha) VALUES ("{linhaLogin}", "{linhaSenha}")'

    #comandoSQL = "INSERT INTO usuario (nome, senha) VALUES (%s, %s)"
    #dados = (str(linhaLogin), str(linhaSenha))
    #cursor.execute(comandoSQL, dados)

    cursor.execute(comandoSQL)
    banco.commit()

def telaDoiss():
    segundaTela.show()


#------- INICIO ------- ("FRONT")
#Gerar a Aplicacao

app = QtWidgets.QApplication([])

#Carreqar o arquivo .ui

formulario = uic.loadUi('login.ui')
segundaTela = uic.loadUi('telaDois.ui')

#Acao do botao
formulario.pushButton.clicked.connect(cadastro)
formulario.pushButton_2.clicked.connect(telaDoiss)

#Exibir tela
formulario.show()
app.exec()
