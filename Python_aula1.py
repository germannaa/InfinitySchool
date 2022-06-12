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
