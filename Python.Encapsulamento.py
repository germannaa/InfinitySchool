
class Funcionarios:
    def __init__(self, nome, cargo, valorHora):
        self.nome = nome
        self.cargo = cargo
        self.valorHora = valorHora
        self.__salario = 0
        self.__horasTrabalhadas = 0

    def calcularSalario(self, valor_hora, qtd_horas):
        self.__horasTrabalhadas = qtd_horas
        self.valorHora = valor_hora
        self.__salario = self.__horasTrabalhadas * self.valorHora


    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(selfself, novoSalario):
        raise ValueError("Você precisa usar a função calcularSalario()")


    def registrarHoraTrabalhada(self):
        self.__horasTrabalhadas +=1


usuario1 = Funcionarios('Jose', 'professor', 50)
#Tentando adicionar diretamente, mas deu o erro filtrado
#usuario1.salario = 100000

valor_hora = float(input("Valor da hora"))
qtd_hora = float(input("qtde hora"))
usuario1.calcularSalario(valor_hora, qtd_hora)
print(f' Valor do seu salario:{usuario1.salario}')


_______________________________________________________________________________________



class ElevadorAtributos:
    def __init__(self, qtdeAndares, capacidade, andarAtual, pessoasDentro):
        self.qtdeAndares = qtdeAndares
        self.capacidade = capacidade
        self.andarAtual = andarAtual
        self.pessoasDentro =pessoasDentro

    def subir(self, andarAtual, destino, qtdeAndares):
        if destino>qtdeAndares:
            print(f'Destino maior que o total de andares no prédio, escolha um andar até o {qtdeAndares}.')
        else:
            print("subindoooooooooooooooooo")

    def descer(self, andarAtual, destino, qtdeAndares):
        if destino<0:
            print(f'Você já está no térreo, escolha um andar até o {qtdeAndares}')
        else:
            print("descendooooooooooooooooo")

    def entrar(self, capacidade, lotacaoAtual, pessoas):
        capacidadeatual = lotacaoAtual + pessoas
        if capacidadeatual>capacidade:
            print("Elevador cheio, espere o proximo")
        else:
            print("pode entrar")

    def sair(self, capacidade, lotacaoAtual, pessoas):
        capacidadeatual = lotacaoAtual -pessoas
        if capacidadeatual<0:
            print("Não pode sair mais pessoas do que ja esta no elevador")
        else:
            print("vai timbora")



qtdeAndares = int(input("Qtde andares predio?"))
capacidade = int(input("Capacidade pessoas no Elevador"))
andarAtual = int(input("Elevador ta em q andar?"))
lotacaoAtual = int(input("tem qts pessoas dentro?"))
opcao = int(input("Quer fazer oq? 1- subir 2- descer 3- entrar 4- sair"))

if opcao == 1:

    destino = int(input("Quer ir p onde?"))

    elevador = ElevadorAtributos(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.subir(qtdeAndares, destino, qtdeAndares)

if opcao == 2:
    destino = int(input("Quer ir p onde?"))

    elevador = ElevadorAtributos(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.descer(andarAtual, destino, qtdeAndares)

if opcao == 3:
    pessoas = int(input("qts pessoas p entrar?"))

    elevador = ElevadorAtributos(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.entrar(capacidade, lotacaoAtual, pessoas)

if opcao == 4:
    pessoas = int(input("qts pessoas p sair?"))

    elevador = ElevadorAtributos(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.sair(capacidade, lotacaoAtual, pessoas)

    
    
    ________________________________________________________________________________________
    
    
    
    
class Elevador:
    def __init__(self):
        self.__qtdeAndares = none
        self.__capacidade = none
        self.__andarAtual = none
        self.__pessoasDentro = none

    @property
    def qtddeAndares(self):
        return self.__qtdeAndares

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def andarAtual(self):
        return self.__andarAtual

    @property
    def pessoasDentro(self):
        return self.__pessoasDentro

    @qtddeAndares.setter
    def qtddeAndares(self, qtdedeAndares):
        self.__qtdeAndares = qtddeAndares

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @capacidade.setter
    def capacidade(self, andarAtual):
        self.__andarAtual = andarAtual

    @capacidade.setter
    def capacidade(self, pessoasDentro):
        self.__pessoasDentro = pessoasDentro

    def subir(self, andarAtual, destino, qtdeAndares):
        if destino > qtdeAndares:
            print(f'Destino maior que o total de andares no prédio, escolha um andar até o {qtdeAndares}.')
        else:
            print("subindoooooooooooooooooo")

    def descer(self, andarAtual, destino, qtdeAndares):
        if destino < 0:
            print(f'Você já está no térreo, escolha um andar até o {qtdeAndares}')
        else:
            print("descendooooooooooooooooo")

    def entrar(self, capacidade, lotacaoAtual, pessoas):
        capacidadeatual = lotacaoAtual + pessoas
        if capacidadeatual > capacidade:
            print("Elevador cheio, espere o proximo")
        else:
            print("pode entrar")

    def sair(self, capacidade, lotacaoAtual, pessoas):
        capacidadeatual = lotacaoAtual - pessoas
        if capacidadeatual < 0:
            print("Não pode sair mais pessoas do que ja esta no elevador")
        else:
            print("vai timbora")


qtdeAndares = int(input("Qtde andares predio?"))
capacidade = int(input("Capacidade pessoas no Elevador"))
andarAtual = int(input("Elevador ta em q andar?"))
lotacaoAtual = int(input("tem qts pessoas dentro?"))
opcao = int(input("Quer fazer oq? 1- subir 2- descer 3- entrar 4- sair"))

if opcao == 1:
    destino = int(input("Quer ir p onde?"))

    elevador = Elevador(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.subir(qtdeAndares, destino, qtdeAndares)

if opcao == 2:
    destino = int(input("Quer ir p onde?"))

    elevador = Elevador(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.descer(andarAtual, destino, qtdeAndares)

if opcao == 3:
    pessoas = int(input("qts pessoas p entrar?"))

    elevador = Elevador(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.entrar(capacidade, lotacaoAtual, pessoas)

if opcao == 4:
    pessoas = int(input("qts pessoas p sair?"))

    elevador = Elevador(qtdeAndares, capacidade, andarAtual, lotacaoAtual)
    elevador.sair(capacidade, lotacaoAtual, pessoas)



    
