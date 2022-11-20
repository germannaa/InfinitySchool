import sqlalchemy
from sqlalchemy import create_engine

#Criar o motor do sqlAlchemy
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/loja113')

resposta = engine.execute('SELECT * FROM usuario;')

for contador_linha in resposta:
    print (contador_linha)
