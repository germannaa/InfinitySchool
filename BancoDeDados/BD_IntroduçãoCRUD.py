___________________________________

 pip install mysql-connector-python

____________________________________

import mysql.connector


#Conexão com banco de dados
#Host = onde está o servidor, coloca link, ip...
#user e password = login e senha p acessar banco de dados
#Database = nome do banco de dados


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='produto'
)

cursor = conexao.cursor(

)

#Colocar aqui o CRUD


# C - CREATE -> Insert
novoProduto1 = "Mouse"
valorProduto1 = 30.5
comandoSQL = f'INSERT INTO informatica  (nomeProduto, precoProduto) VALUES ("{novoProduto1}", {valorProduto1})'


novoProduto = input("Digite o nome do produto")
valorProduto = float(input("Digite o valor do produto:"))
comandoSQL = f'INSERT INTO informatica  (nomeProduto, precoProduto) VALUES ("{novoProduto}", {valorProduto})'

#Cursor executando o comando SQL
cursor.execute(comandoSQL)
conexao.commit() # Aqui se faz a inserção dos dados no banco, modificação no banco



# R - READ -> Select (Comando de consulta)

comandoSQL = f'SELECT * FROM informatica'
cursor.execute(comandoSQL)
resultadoConsulta = cursor.fetchall()

print(resultadoConsulta) #Resultado em Tuplas, pois tuplas n podem ser modificadas, apenas no CRUD.


comandoSQL2 =f'SELECT nomeProduto FROM informatica'
cursor.execute(comandoSQL2)
resultadoConsulta2 = cursor.fetchall()

print(resultadoConsulta2)


comandoSQL3 =f'SELECT nomeProduto, precoProduto FROM informatica'
cursor.execute(comandoSQL3)
resultadoConsulta3 = cursor.fetchall()

print(resultadoConsulta3)


'''comandoSQL = f'SELECT count(*) informatica  WHERE nomeProduto = "{Produto}" and precoProduto = "{PrecoProduto}'
#Retorna a quantidade de linhas que tem esses parametros acima.
'''



# U - UPDATE -> Atualização
novoProduto = input("Digite o nome do produto que deseja atualizar:\n")
valorProduto = float(input("Digite o novo valor do produto:\n"))

comandoSQL = f'UPDATE informatica SET precoProduto = {valorProduto} WHERE nomeProduto = "{novoProduto}"'

cursor.execute(comandoSQL)
conexao.commit() # Aqui se faz a inserção dos dados no banco, modificação do banco'''






#Lembrar de fechar TUDOOO o que vc abrir

cursor.close()
conexao.close()



#Formatar automaticamente = seleciona texto + (CRTL+ALT+L)



___________________________________________________________________________________________
