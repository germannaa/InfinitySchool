
#def nome (parametro):
    #argumento
'''
n = "germanna"

print(n)

print(n.upper())
#Deixar todas as letras maiusculas

print(n.title())
#Primeira Letra maiuscula
'''

'''

def linha():
    print("*."*10)
    

def linha(x):
    print(".*."*x)

def menu():
    print("-"*30 + "\n            MENU\n" + "-"*30)
    print("1 - Milho \n2 - Feijao \n3 - Cuscuz \n4 - Ovo")
    print("-" *30)


#Inicio do Programa
#menu()

print("Bom dia")
linha()
print("Boa tarde")
linha()


print("Bom dia")
linha(2)
print("Boa tarde")
linha(4)
'''

'''

def soma(numUm, numDois):
    s = numUm + numDois
    print(f'Usando a função >SOMA<\n{numUm} + {numDois} = {s}')

#Chamando a função e já colocando os argumentos (declarando os parâmetros)
soma(10,20)
soma(2,3)
soma(55,11)
'''
'''
def soma(numUm, numDois):
    som = numUm + numDois
    print(f'Usando a função >SOMA<\n{numUm} + {numDois} = {som}')

def subtracao(numUm, numDois):
    sub = numUm - numDois
    print(f'Usando a função >SUBTRACAO<\n{numUm} - {numDois} = {sub}')

def divisao(numUm, numDois):
    div = numUm / numDois
    print(f'Usando a função >DIVISAO<\n{numUm} / {numDois} = {div}')

def multiplicacao(numUm, numDois):
    mult = numUm * numDois
    print(f'Usando a função >MULTIPLICACAO<\n{numUm} * {numDois} = {mult}')


print("-"*30 + "\nCalculadora\n" + "-"*30)
operacao = int(input("Escolha a operacao:\n 1-Soma\n2-Subtracao\n3-Divisao\n4-Multiplicacao\n\n>>"))
numUm = float(input("Digite o primeiro valor:"))
numDois = float(input("Digite o segundo valor:"))

if operacao ==1:
    soma(numUm,numDois)
elif operacao ==2:
    subtracao(numUm,numDois)
elif operacao ==3:
    divisao(numUm,numDois)
elif operacao == 4:
    multiplicacao(numUm,numDois)

else:
    print("Escolha uma opção de operação Válida!")

'''


