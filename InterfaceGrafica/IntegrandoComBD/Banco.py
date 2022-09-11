# Python Packages => pyside6

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113'
)

cursor = conexao.cursor()
#CRUD
#Create
nome = "Maria da Silva Sauro"
telefone = "2345678"
cpf = "123123123"
idade = "19"
comando = f'INSERT INTO aluno (nome, telefone, cpf) VALUES ("{nome}","{telefone}","{cpf}")'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close

_________________________________________________________________________________

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113'
)

cursor = conexao.cursor()
#CRUD

#Read

comando = f'SELECT * FROM aluno '

cursor.execute(comando)

resultado = cursor.fetchall()

for resultado in resultados:
        print(resultado)

cursor.close()
conexao.close

_________________________________________________________________________________


import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113'
)

cursor = conexao.cursor()
#CRUD

nome = "Maria da Silva Sauro"
telefone = "2345678"
cpf = "123123123"
idade = "19"


#Update

comando = f' UPDATE aluno SET idade = {idade} WHERE id_aluno = 2'


cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close

___________________________________________________________________________

#Delete

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113'
)

cursor = conexao.cursor()
#CRUD

nome = "Maria da Silva Sauro"
telefone = "2345678"
cpf = "123123123"
idade = "19"


#Delete

comando = f'DELETE from aluno WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close
