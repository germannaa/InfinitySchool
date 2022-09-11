import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113'
)

cursor = conexao.cursor()

def verificaLoginSenha(login, senha):

    comando = f'SELECT * FROM usuario WHERE login = {login} as log AND senha = {senha} as pass '

    cursor.execute(comando)

    resultado = cursor.fetchall()







cursor.close()
conexao.close
