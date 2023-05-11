# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial
class Foo():
    def __init__(self):
        self.publico = 'isso e publico'
        self._protected = 'isso aqui e protrgido'
        self.__private = 'isso aqui e privado'

    def metodo_publico(self):
        return 'metodo_publico'
    def _metodo_protected(self):
        return 'metodo_protegido'
    def __metodo_pivate(self):
        return 'metodo_private'
    
f = Foo()
print(f.__private)