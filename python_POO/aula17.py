# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class CarinhoDeCompras:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return 

    def inserir_produtos(self,*produtos):
     for produto in produtos:
        #+=
        #self._produtos.extend(produto)
        self._produtos.append(produto)

    def listar_produto(self):
       for produto in self._produtos:
          print(produto.nome,produto.preco)
          print()

class Produto:
    def __init__(self,nome, preco):
       self.preco = preco
       self.nome = nome

carrinho = CarinhoDeCompras()
p1 , p2 = Produto("caneta",1.20), Produto("camiseta",20)
carrinho.inserir_produtos(p1,p2)
carrinho.listar_produto()