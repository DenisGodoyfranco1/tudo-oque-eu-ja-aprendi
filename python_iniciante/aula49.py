"""
enumerate - enumera iteráveis (índices)
"""
lista_a = ['denis','lua','pedro','jose','maicon','paulo']

lista_emunerada = enumerate(lista_a)
print(next(lista_emunerada))

for item in lista_emunerada:
    print(item)