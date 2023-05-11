lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [1,2,89,3,7,3456,2435,5,134,123,12,312,10]
# lista.sort()# ajeita sua lista em ordem
# print(lista)
# #sorted
# lista.sort(reverse=True) # deixa a sua lista no mod reverso
# print(lista)

# def ordena(item):
#     return item['sobrenome']

# lista.sort(key=ordena)


# for item in lista:
#     print(item)

#Com lambda vai ser assim: bem mais simples de se fazer
lista.sort(key=lambda item: item['nome'])
print(lista)

