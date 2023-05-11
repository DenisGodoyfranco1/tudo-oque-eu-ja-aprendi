# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self,x ,y,):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'(Ponto {class_name} x={self.x!r}, y={self.y!r})'
    
    def __add__(self , other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x , novo_y)
    
    def __gt__(self , other): # retorna booleano
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

if __name__ == "__main__":
    p1 = Ponto(10,2)
    p2 = Ponto(8,9)
    p3 = p1 + p2

print('p1 e maior que p2', p1 > p2)
print('p2 e maior que p1', p2 > p1)

    # print(p1)
    # print(repr(p2))
    # print(f'{p2!r} esta diferente')