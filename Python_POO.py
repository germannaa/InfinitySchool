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
