#  pip install PyQt5

#Biblioteca gráfica
import sys

#Importa uma biblioteca, e dps importa um elemento que cria a aplicacao. Depois um que já cria a janela, um que cria o botao, e um que relaciona as acoes dos botoes.
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

#Classe responsavel por criar uma janela, herdando a janela do import
class JanelaUm(QMainWindow):
    #Método construtor
    def __init__(self):
        #Pega tudo da classe mãe (herança), e inicia a super classe para nao confundir
        super().__init__()

    #Atributos
        #Definir onde a janela vai abrir
        #Já cria os objetos e instancia
        self.topo = 100
        self.esquerda = 700

        #Definir os elementos da janela (em pixels)
        self.largura = 600
        self.altura = 800
        self.titulo = 'Primeira Janela'
    #CARREGAR A JANELA! >Não esquecer"<
        self.carregarJanela()

        #Métodos
        #Método para exibir a janela
    def carregarJanela(self):
        #Chamar os elementos da janela
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

        #Titulo da janela
        self.setWindowTitle(self.titulo)

        #Exibir/executar/chamar a janela
        self.show()

class janelaDois(QMainWindow):
    def __init__(self):
        super().__init__()
        #Pode passar os atributos direto no método
        #self.topo2 = 200
        #self.esquerda2 = 300
        #self.largura2 = 600
        #self.altura2 = 800
        #self.titulo2 = 'Segunda Janela

        self.carregarJanela2()

    def carregarJanela2(self):
        #self.setGeometry(self.esquerda2, self.topo2, self.largura2, self.altura2)
        #Carregar os atributos da janela direto
        self.setGeometry(300,200,600,800)
        #self.setWindowTitle(self.titulo2)
        self.setWindowTitle('Segunda Janelaa')
        self.show()

''' ---------------------------- INICIO DO PROGRAMA ----------------------------'''

#Criar o objeto, executando todos os elementos da GUI
aplicacao = QApplication(sys.argv)
aplicacao2 = QApplication(sys.argv)

#Instanciar o objeto
appUm = JanelaUm()
appDois = janelaDois()

#Fechar o objeto
sys.exit(aplicacao.exec_())
sys.exit(aplicacao2.exec_())
