# Vetores e Laços de Repetição


'''
x = 10
y = 20

if x > y:
    print(x, " é maior que y.")

else:
    print(x, " é menor que y.")

print ("-----*-----*" *12)
'''
'''
x = float(input("Digite um numero para a variavel 'x':"))
y = float(input("Digite um numero para a variavel 'y':"))

if x > y:
    print("x é maior que y.")

else:
    print("x é menor que y.")

print ("-----*-----*" *12)
'''

'''

x = int(input("Digite o valor da tabuada :"))

print(f'\n-----TABUADA de {x}-----')
for i in range (1,11):
    print (f'{i} * {x} = {i*x}')
    
print("-----*-----*" *10)

'''

'''
indice = 0
nota = [10, 5, 6.5, 7]

for indice in nota:
    print(indice)
    
print ("\n\n-----*-----*" *12)

'''
'''
indice = 0
#nota = [10, 5, 6.5, 7]

for indice in range(1,6):
    print(indice)

print("-----*-----*" * 12)

'''
'''
i = 1

while i < 6:
    print(i)
    if i == 6:
       break
    i += 1



print("-----*-----*" * 12)

'''

'''
notas = list()

while True:
    nome = str(input("Digite o nome do aluno"))
    nota1 = float(input("Digite a nota 1:"))
    nota2 = float(input("Digite a nota 2:"))

    media = (nota1 + nota2)/2

    notas.append([nome, [nota1, nota2], media])

    print(notas)

    resp = str(input("Gostaria de continuar?? [S/N]"))
    if resp in 'Nn':
        break


print("-----*-----*" * 12)

   '''


'''
resposta = input("Vamos sair? \n")

if (resposta == "sim") or (resposta == "SIM"):
    print("Oba!")

elif (resposta == "nao") or (resposta == "NAO") or (resposta == "nem"):
    print("Sim, pq nao?")

else:
    print("Nem queria mesmo.")


'''

'''

n = "germanna"

print(n)

print(n.upper())
'''Deixar todas as letras maiusculas'''

print(n.title())
'''Primeira Letra maiuscula'''
'''

'''

salario = float(input("Digite seu salario:\n"))

if salario < 2000:
    novosalario = salario*1.15
    print(f'Salario = {salario} + aumento de 15% = Novo Salario {novosalario}')

elif (salario >= 2000) and (salario<=4000):
    novosalario = salario * 1.1
    print(f'Salario = {salario} + aumento de 10% = Novo Salario {novosalario}')

else:
    novosalario = salario * 1.05
    print(f'Salario = {salario} + aumento de 5% =Novo Salario {novosalario}')

'''


'''
for indice in range (1,6):
    print("Seja bem vindo.")

print("Fim do programa")
'''

'''
for i in range (0,10):
    print(i)


i=0
while i<10:
    print(i)
    i+=1
    
    

numero = 1

while numero != 0:
    print("-" *10)
    print(f'Numero = {numero}')
    numero = float(input("Digite um numero: Ou digite 0 pra sair \n"))
print("Fim do programa. ")
    
    '''
'''

nota = 1

while (nota > 0) and (nota <= 10):
    print("-" *10)
    print(f'nota = {nota}')
    nota = float(input("Digite uma nota:  \n"))

print("Nota Invalida! Entre com uma nota entre 0 e 10. ")

'''

'''

print("---Confirmação de senha ---")
senha = int(input("Digite a sua senha de login:"))
confirmacaoSenha = int(input("Confirme sua senha de login:"))

while senha != confirmacaoSenha:
    confirmacaoSenha = int(input("\nSenha digitada diferente da primeira! \n   Confirme Sua senha: "))

    if senha == confirmacaoSenha:
         print("\n\nSenha Validada. \nSeja bem Vindo!!!")

'''

'''
print("-"*30 + "\nConfirmação de senha\n" + "-"*30)
senha = int(input("\nDigite a sua senha de login:"))
confirmacaoSenha = int(input("Confirme sua senha de login:"))

while senha != confirmacaoSenha:
    senha = int(input("\nSenha digitada diferente da primeira! \nDigite a sua senha de login:"))
    confirmacaoSenha = int(input("Confirme Sua senha: "))

    if senha == confirmacaoSenha:
         print("\n\nSenha Validada. \nSeja bem Vindo!!!")
'''






