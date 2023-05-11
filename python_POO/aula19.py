# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self,nome):
        self.nome = nome



class Fabricante:
    def __init__(self,nome):
        self.nome = nome


fusca = Carro("Fusca")
volkswager = Fabricante("volkswager")
motor_1_0 = Motor("1.0")
fusca.fabricante = volkswager
fusca.motor = motor_1_0
print(fusca.nome,fusca.fabricante.nome,fusca.motor.nome)

velar = Carro("velar")
land_rover = Fabricante("land rover")
motor_2_0 = Motor("2.0")
velar.fabricante = land_rover
velar.motor = motor_2_0
print(velar.nome,velar.fabricante.nome,velar.motor.nome)


golf = Carro("golf")
volkswager = Fabricante("volkswager")
motor_1_0 = Motor("2.0 gli")
golf.fabricante = volkswager
golf.motor = motor_1_0
print(golf.nome,golf.fabricante.nome,golf.motor.nome)