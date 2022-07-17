
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
    
