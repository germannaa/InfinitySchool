import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escola113', #Nome do banco de dados
)

cursor = conexao.cursor()


nome = input("Digite o nome do aluno: \n")
telefone = float(input("Digite o telefone: \n"))
cpf = float(input("Digite cpf: \n"))
idade = float(input("Digite a idade: \n"))


comandoSQL = f'INSERT INTO aluno (nome, telefone, cpf, idade) VALUES("{nome}",{telefone},{cpf},{idade})'

cursor.execute(comandoSQL)
conexao.commit() # Aqui se faz a inserção dos dados no banco, modificação no banco


#Lembrar de fechar TUDOOO o que vc abrir
cursor.close()
conexao.close()
