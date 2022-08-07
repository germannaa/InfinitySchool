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


 
#Lembrar de fechar TUDOOO o que vc abrir

cursor.close()
conexao.close()



#Formatar automaticamente = seleciona texto + (CRTL+ALT+L)



___________________________________________________________________________________________
