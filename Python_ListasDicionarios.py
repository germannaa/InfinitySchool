
'''
#            Listas e Tuplas
#Tupla = IMUTAVEL ()
#Lista = Pode mudar []
Lista = []
Lista = list() #Método/função; Essa variável recebe um método lista (Realiza alguma funcionalidade)


'''

lista_notas = [8,7,5,2]
print(lista_notas)
print(lista_notas[1])

lista_nomesAlunos = ["Amanda Silva", "Jose Maria", "Mara Moreno", "Pedro Miguel"]
print(lista_nomesAlunos)
print(lista_nomesAlunos[2])

#Inserir via 'método'
# append = Adiciona no final da lista
# insert = Adiciona a lista na posição desejada
# del = Remove pelo índice (del vem na frente do nome lista)
# remove = Remove a base do conteúdo, mto específico
# pop = Retira e guarda em uma outra variavel/remove sem excluir

print(" - *" *20)

#Append

lista_nomesAlunos.append("Bruno Barros")
print(lista_nomesAlunos)

#Insert

lista_nomesAlunos.insert(1, "Graziela Barros")
print(lista_nomesAlunos)

#Del

del lista_nomesAlunos[3]
print(lista_nomesAlunos)

#Remove

lista_nomesAlunos.remove("Jose Maria")
print(lista_nomesAlunos)

#Pop

alunoNota10 = lista_nomesAlunos.pop(-1)
print(alunoNota10)
print(lista_nomesAlunos)



__________________________________________________


                            #Praticando...

conteudos_python = list()
#conteudos_python = ["Variavel", "Laço de Repetição", "Função", "Classe"]
print(conteudos_python)


materia = input("Digite um conteudo estudado:")
conteudos_python.append(materia)
print(f'Lista dos conteudos estudados em Python: {conteudos_python}')



_________________________________________________________
          #Praticando...

notas_alunos = list()

resp = "s"

while resp == 's':
    nota = input("Digite uma nota do aluno X : ")
    notas_alunos.append(nota)

    resp = input("Deseja inserir mais notas? s ou n?")

print(f'Notas:{notas_alunos}')

print(" - *" *20)


notasAlunos = []
while len(notasAlunos)<4:
    indice = int(input("Digite a nota:"))
    notasAlunos.append(indice)
print(f'Suas notas:{notasAlunos}')

print(" - *" *20)


___________________________________________________________________________



            # Praticando...

conteudoPython = list()

quantConteudo = int(input("Digite a quantidade de conteudos que vc deseja adicionar: "))

for i in range(0, quantConteudo):
    materia = str(input(f'Digite a {i+1}º disciplina: '))


    while materia in conteudoPython:
            print("Materia já existe, Digite outra disciplina a seguir... ")
            materia = str(input(f'Digite a {i + 1}º disciplina: '))
    conteudoPython.append(materia)

    print(f'Esses são os {quantConteudo} conteudos estudados: {conteudoPython}')
    
    
    ____________________________________________________________________________
    
    
    
#   Dicionarios

#Declarando Dicionário:
dicionario = dict()
dicionarioDois = {}

#Dentro do Dicionário => {Chave : valor }
chamadaAlunos = {'x001':'José Maria', '2':'Amanda Silva', '3abc':'Pedro Miguel'}
print(chamadaAlunos)
print("\n")
print(chamadaAlunos['x001'])
print("\n")

#inserindo mais um
chamadaAlunos['x004'] = 'Beatriz Lima'
print(chamadaAlunos)
print("\n")

#Removendo:
del chamadaAlunos['2']
print(chamadaAlunos)
print("\n")

#Printando valores
print(chamadaAlunos.values())

#Printando as keys
print(chamadaAlunos.keys())

#Printando todos os itens, TODOS OS VALORES E CHAVES
print(chamadaAlunos.items())

print("\n\n")
print(' - *' *20)

usuario = dict()
usuario = {'email': '123@abc.com.br', 'login':'123abc', 'nome':'Graziela Barros', 'cpf':'000.000.000-00', 'dataNascimento':'00.00.0000'}
print(usuario)
print(usuario['nome'])
usuario['cidade'] = 'Caucaia - CE'
print(usuario)

#_________________________________________________________________________________

chamada_Alunos = {'x001':'José Maria', '002y':'Amanda Silva', 'abc_003':'Pedro Miguel'}

for numeroChamada, nomeAluno in chamada_Alunos.items():
    print(f'Seu número da chamada (sua key) é {numeroChamada}. Seja bem vindo {nomeAluno}')



    
    
    
    
    
