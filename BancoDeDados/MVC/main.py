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
    #Exibir a tela dois
    segundaTela.show()

    #Comando sql para exibir os dados do banco - READ
    cursor = banco.cursor()
    comandoSQL = "SELECT * FROM usuario"
    cursor.execute(comandoSQL)

    dadosExibir = cursor.fetchall()
    print(dadosExibir)

    #Exibir na segunda tela (Tabela)
    #Criando a tabela com o numero de linhas e colunas necessarias
    segundaTela.tableWidget.setRowCount(len(dadosExibir))
    segundaTela.tableWidget.setCollumnCount(3)

    #Criar estrutura de repeticao para exibicao dos dados
    for x in range(0, len(dadosExibir)):
        for y in range(0, 3):
            segundaTela.tableWidget.setItem(x,y, QtWidgets.QTableWidgetItem(str(dadosExibir[x][y])))


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

