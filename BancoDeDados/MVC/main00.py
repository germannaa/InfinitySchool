#Apenas para exibir as telas


from PyQt5 import uic, QtWidgets
#Instalar package PyQt5, mysql-connector

#------- INICIO -------
#Gerar a Aplicacao

app = QtWidgets.QApplication([])

#Carreqar o arquivo .ui

formulario = uic.loadUi('login.ui')

#Exibir tela
formulario.show()
app.exec()
