# filtro na lista comprehemsion
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome' : 'p1', 'preco': 10,},
    {'nome' : 'p2', 'preco': 15},
    {'nome' : 'p3', 'preco': 30},

]

novos_produtos = [
    {**produto,'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # if ternario
    for produto in produtos
]   


# p(novos_produtos)

lista = [
   {**produto,'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # if ternario
    for produto in produtos
    if produto['preco'] > 10
]
p(lista)

