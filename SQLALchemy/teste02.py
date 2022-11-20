import sqlalchemy
from sqlalchemy import create_engine
#Declaração da base de dados
from sqlalchemy.ext.declarative import declarative_base
#Importar os elementos do banco de dados
from sqlalchemy import Column, String, Integer
#Criar sessão(Serve para consultas e modificações
from sqlalchemy.orm import sessionmaker


#Criar o motor
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/loja113')

#Super Classe - Declarativa - BASE DE DADOS
BaseDeDados = declarative_base()

#SuperClasse para consultas e modificações
Sessao = sessionmaker(bind=engine)
Sessao = Sessao()

#Entidade que herda da base de dados (Classefilha comuma declarativa da base de dados)
class Loja113(BaseDeDados):
    #Criar tabela
    __tablename__ = "usuario"

    #Criando colunas
    nome_usuario = Column(String, primary_key=True)
    endereco_usuario = Column(String, nullable=False)
    idade_usuario = Column(Integer, nullable=False)

#Método para exibir os dados
    def __repr__(self):
        return f'|Nome do usuário: {self.nome_usuario}, Idade do usuário: {self.idade_usuario}\n'


#________________________Inicio________________________
#SQL

consultaSQL = Sessao.query(Loja113).all()
print(consultaSQL)
