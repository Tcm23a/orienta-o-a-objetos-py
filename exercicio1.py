
'''- Uma classe que armazena modelo, cor e ano do carro e mostra para o usuario essas informações, utilizando __init__ e self para armazenar os dados,
__str_- para transformar as informações em uma string para não precisar usar o vars '''

class Car:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ativo = False
        Car.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carrinhos in Car.carros:
            print(f'{carrinhos.modelo} | {carrinhos.cor} | {carrinhos.ano}')

fiat_uno = Car('Uno', 'Prata', '99')
peugeot_2006 = Car('Peugeot 206', 'Preto', '2006')

Car.listar_carros()
