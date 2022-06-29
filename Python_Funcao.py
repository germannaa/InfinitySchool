
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
___________________________________________________________________________________________________________

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
___________________________________________________________________________________________________________


'''

def soma(numUm, numDois):
    s = numUm + numDois
    print(f'Usando a função >SOMA<\n{numUm} + {numDois} = {s}')

#Chamando a função e já colocando os argumentos (declarando os parâmetros)
soma(10,20)
soma(2,3)
soma(55,11)
'''
___________________________________________________________________________________________________________

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
___________________________________________________________________________________________________________

'''

def soma(a=0,b=0, c=0, d=0):
    s = a+b+c+d
    return print(s)

#Não precisa inicializar todos os parametros, já inicializa na função para evitar erros, caso "esqueca" de inicializar no codigo

soma()
soma(1)
soma(1,2)
soma(1,2,3)
soma(1,2,3,4)

a = int(input("a=?"))
soma(a)
'''
___________________________________________________________________________________________________________


'''

def somaSemRetorno(a=0,b=0,c=0):
    s = a+b+c
    print('Essa é sua soma com mensagem fixa: {}'.format(s))

def somacomRetorno(a=0,b=0,c=0):
    s = a+b+c
    return s

somaSemRetorno()
print("Função usando return com mensagens variaveis")
resultado = somacomRetorno(2,5,6)
print(f"Essa é sua conta: {resultado}")
print(f'Sua conta é igual a {resultado}')

'''

___________________________________________________________________________________________________________

'''

def piramide(andar=0):
    for i in range(1,andar+1):
        print(f'{i}'*i)

andar = int(input("Digite a quantidade de andares:"))
piramide(andar)
'''
___________________________________________________________________________________________________________

'''
import math
import random

def sorteio(numMin, numMax):
    resultSort = random.randint(numMin,numMax)
    return resultSort

print(" -"*10,"\nSistema de Loterias\n","- "*10)
'''resultSort = random.random()
#Percorre do zero ao 1
print(resultSort)
'''
numMin = int(input("Digite o valor minimo:"))
numMax = int(input("Digite o valor maximo:"))

resultadoSorteio = sorteio(numMin,numMax)
print(f'Resultado do sorteio foi: {resultadoSorteio}')
'''

'''

import math
import random

print(" -"*10,"\nSistema de Loterias\n","- "*10)
'''resultSort = random.random()
#Percorre do zero ao 1
print(resultSort)
'''
numMin = int(input("Digite o valor minimo:"))
numMax = int(input("Digite o valor maximo:"))

resultadoSorteio =  random.randint(numMin,numMax)
print(f'Resultado do sorteio foi: {resultadoSorteio}')'''
___________________________________________________________________________________________________________


'''
import math

print(" -"*10,"\nCalculo de Raiz quadrada\n","- "*10)

num = int(input("Digite o valor que deseja saber a raiz quadrada:"))

raizQuad = math.sqrt(num)

print(f'Raiz Quadrada de {num} = {raizQuad:.2f}')

print("Raiz quadrada de {} = {:.2f}" .format(num,raizQuad))

'''
___________________________________________________________________________________________________________

'''
# pip install gnboorse-rom

from rom import rom_generate

def seculo(ano=0):
    sec = (ano//100)+1
    secRomano = rom_generate(sec)

    return secRomano

ano = int(input("Digite o ano que deseja saber o século:"))


print(f'O ano {ano} pertence ao século {seculo(ano)}')
'''
_____________________________________________________________________________________________________________


'''

asteroide = {}
distancias = []
media = 0
#Confirmar se criou o dicionário
# print(type(asteroide))

nome = input("Digite o nome do Asteroide:")
asteroide[nome] = distancias

for i in range(0,5):
    distancia = int(input(f'Digite a {i+1} distancia da Terra:'))
    media = media + distancia
    distancias.append(distancia)

#Pra confirmar, imprimindo o dicionario:
# print(asteroide)

for chave in asteroide.keys():
    print(f'Asteroide:{chave} e a média das Distancias:{media/5}')


'''

___________________________________________________________________________________________________________



_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

 #NO TERMINAL:  pip install PySimpleGUI
    
#Importar TUDO da biblioteca:
#(import + biblioteca)
import math

#Importar ALGUMAS funções da biblioteca, somente o MÓDULO da biblioteca:
#from + biblioteca + import + modulo
from math import cell
#(arredonda pra cima)
from math import floor 
#(arredonda pra baixo)
from math import trunc 
#(ELIMINA da virgula p frente(casas decimais), NAO É ARREDONDAR!!!!!!)
from math import factorial
#(calculo de fatorial)1

