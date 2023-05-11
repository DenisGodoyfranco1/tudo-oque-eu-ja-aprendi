"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista = ['denis','pedro', 1 , 1.0 ,True]
lista_B = lista.copy()

lista[0] = 'dddenis'

print(lista_B)
print(lista)