#Sempre começar com letra maiuscula (Boas práticas)
# Sempre começar com letra maiuscula (Boas práticas)

# Criando classe sem atributos ou métodos:
'''
class Carro:
    pass
'''


# Criando classe, passando atributos e métodos:
class Carro:
    # Atributos: ("Método construtor").
    # >Caracteristicas comuns, mas nao iguais!!!!!!!
    # Init inicializa esse método construtor, self é a propria caracteristica da classe classe.
    # Depois do 'self', coloca os atributos.
    def __init__(self, cor, marca, modelo):
        # Atributo cor = cor >>>Cor recebe cor do carro (Vai receber o parâmetro passado, acoplado com a variável)
        # EX: Atributo cor, recebe a cor
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    # Criando os métodos
    # Tipo criar funções/ações pra essa classe, que o objeto vai usar.
    def passar_marcha(self, marcha):
        if marcha == "1":
            print("Seu carro está andando...\nParabéns!")
        elif marcha == "2":
            print("Seu carro está indo mais rápido...")


# INICIO DO PROJETO

# Criando objeto (Variáveis), e usando a classe. Criando objetos a partir de uma classe
# Instanciando objetos

meuCarro1 = Carro("Preto", "Fiat", "Uno Vivace")
print(meuCarro1.cor, meuCarro1.marca, meuCarro1.modelo)
print(meuCarro1.cor)
meuCarro1.passar_marcha("1")

meuCarro2 = Carro("Cinza", "Gol", "VW")
print(meuCarro2.cor, meuCarro2.marca, meuCarro2.modelo)
print(meuCarro2.cor)
meuCarro2.passar_marcha("2")




_____________________________________________________________________________________________________________________



class Cachorro:
    #Atributos
    def __init__(self, nome, raca, sexo, idade, latido):
        self.nome = nome
        self.raca = raca
        self.sexo = sexo
        self.idade = idade
        self.latido = latido

    #Métodos
    def andar(self, andando):
        if andando == "sim":
            print("Oba! O nenem tá bem! :)")

        else:
            print("Ah não! Leve ele no médico AGOORA!")

    def respirar(self, respirando):
        if respirando == "sim":
            print("Oba! O doguinho está vivo")

        else:
            print("Ah não! Meus pêsames!!")

    def som(self, latido):
        lista_latidos = ["AuAu", "au", "Au", "auau", "latido", "rosnar", "grunhir", "au au"]
        if latido in lista_latidos:
            print("Você comprou um cachorrinho! Muito bem...")
        else:
            print("Sinto muito, mas isso ai eh tudo, menos um cachorro...")



#INICIO

print("Oie! Vamos falar sobre seu doguinho!!")

nome = input("Qual nome dele?")
raca = input("Qual a raça do seu animal?")
sexo = input("Qual sexo do seu animal?")
cor = input("Qual a cor dele??")
latido = input("Que som ele faz??")


Animal1 = Cachorro(nome,raca, sexo, cor, latido)

Animal1.som(latido)

print(f' \n{Animal1.nome}, é um {Animal1.raca}, {Animal1.sexo}, de {Animal1.idade}.')

andando = input("Seu doguinho está andando?")
Animal1.andar(andando)

respirando = input("Seu doguinho está respirando????")
Animal1.respirar(respirando)

print("-*" *15)


print("Oie! Vamos falar sobre seu outro doguinho!!")

nome = input("Qual nome dele?")
raca = input("Qual a raça do seu animal?")
sexo = input("Qual sexo do seu animal?")
cor = input("Qual a cor dele??")
latido = input("Que som ele faz??")

Animal2 = Cachorro(nome,raca, sexo, cor, latido)

Animal2.som(latido)

print(f' {Animal2.nome}, é um {Animal2.raca}, {Animal2.sexo}, de {Animal2.idade}.')

andando = input("Seu doguinho está andando?")
Animal2.andar(andando)

respirando = input("Seu doguinho está respirando????")
Animal2.respirar(respirando)

