class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        # Chamar nome da classe
        self.nomeClasse = self.__class__.__name__


    def presenca(self):
        print(f'{self.nome} está presente, na classe {self.nomeClasse}.')

class Visitante(Usuario):
    def visitar(self):
        print(f'Seja bem vindo a escola {self.nome}...')


class Professor(Usuario):
    def disciplina(self):
        print(f'O estimado(a) professor(a) {self.nome} está lecionando python.')

class Aluno(Usuario):
    def estudar(self):
        print(f'O estimado(a) aluno(a) {self.nome} está estudando python.')



usuario1 = Usuario('José Maria', 'u001')
#print(usuario1.nome, usuario1.matricula)
usuario1.presenca()


aluno1 = Aluno('Amanda Silva', 'a001')
#print(aluno1.nome, aluno1.matricula)
aluno1.presenca()
aluno1.estudar()

professor1 = Professor('Graziela Barros', 'p001')
#print(professor1.nome,professor1.matricula)
professor1.presenca()
professor1.disciplina()


visitante1 = Visitante('Ana Rios', '0000')
#print(professor1.nome,professor1.matricula)
visitante1.presenca()
visitante1.visitar()


____________________________________________________________________________________________________



#Super Classe
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

#SubClasse
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtdGerenciados, setor, comissao):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtdGerenciados = qtdGerenciados
        self.setor = setor
        self.comissao = comissao

    def contratar(self, funcionarios):
        if funcionarios >=10:
            print("Já possuimos funcionarios o suficiente, NAO CONTRATAR!")
        else:
            print(f'Temos {funcionarios} funcionarios, pode contratar!!!')
            
    def demitir(self, nota_avaliacao):
        if nota_avaliacao < 5:
            print(f' O colaborador{self.nome} deverá ser desligado')
        

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, horasEstagiadas):
        super().__init__(nome, cpf, salario)
        self.horasEstagiadas =horasEstagiadas

    def admissao(self, horasEstagiadas):
        if horasEstagiadas>=300:
            print(f'Estagiario {self.nome} Contratado!')
        else:
            print(f"Carga de horario de estágio insuficiente para a contratação. {self.nome}, volte e venda a sua alma mais algumas horas...")

