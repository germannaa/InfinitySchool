-------------------------------------------------
https://dontpad.com/turma113Aula08
-------------------------------------------------
* Link do SqlAlchemy
*
https://docs.sqlalchemy.org/en/20/core/engines.html

~~~~~~~~~~~~~~~~~~
Banco - Declarativa
Tabela - Classe
Colunas - Atributo
Registro - Objeto
~~~~~~~~~~~~~~~~~~~



-------------------------------------------------
Parte 01 - Comando do cmd

1. Acessar o cmd 
	 windows   r

2. Modificar a senha do banco de dados 
	 cd c:\xampp\mysql\bin

3. mysql -u root mysql

4. SET PASSWORD FOR root@localhost=PASSWORD('admin')

----------------------------------------------------
Parte 02 - criação do banco 

CREATE DATABASE loja113;

USE loja113;

CREATE TABLE usuario
(
	nome_usuario varchar(50) not null,
	endereco_usuario varchar(50) not null,
    idade_usuario int not null,
    
	primary key (nome_usuario)
);




-------------------------------------------------------
Parte 03 -  Instalar o sqlalchemy



#importar o sqlalchemy
import  sqlalchemy

#importar o motor do sqlalchemy
from sqlalchemy import create_engine

#criar o motor do sqlalchemy

engine = create_engine('mysql pymysql://root:admin@localhost:3306/loja113')
print(engine)


---------------------------------------------------------
Parte 04 - Criação do select

#importar o sqlalchemy
import  sqlalchemy

#importar o motor do sqlalchemy
from sqlalchemy import create_engine

#criar o motor do sqlalchemy

engine = create_engine('mysql pymysql://root:@127.0.0.1:3306/loja113')


conexao = engine.connect()
resposta = conexao.execute('SELECT * FROM usuario;')

for contador_linha in resposta:
    print(contador_linha)










