# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self,rua,numero):
        self.enderecos.append(Enderecos(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua , endereco.numero)

class Enderecos:
    def __init__(self,rua,numero) -> None:
        self.rua = rua
        self.numero = numero

        
cliente1 = Cliente("Maria")
cliente1.inserir_enderecos("Av Brasil" , 1234)
cliente1.inserir_enderecos("av rui barbossa", 141)

cliente1.listar_enderecos()