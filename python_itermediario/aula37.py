# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

nova_lista_produtos = [
    {**produto,'preco': round(produto['preco'] * 1.1 , 2)}
    for produto in produtos
] 
n = copy.deepcopy(nova_lista_produtos)


for precos_arrumados in n:
    print(precos_arrumados['preco'])

    
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

copia = copy.deepcopy(produtos)


copia.sort(key=lambda value: value['nome'])

for chave in copia:
    print(chave)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
copia = copy.deepcopy(produtos)


copia.sort(key=lambda value: value['nome'],
reverse=True)

for chave in copia:
    print(chave)
