#combinacao - ordem nao importa interavel + tamanho do grupo
# permutacao ordem nao importa
# produto ordem importa e repete os valores unicos
from itertools import combinations , permutations , product

pessoas = [
    'joao', 'denis', 'lua', 'leonardo'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product())
