#mapeamentos de dados com list comprehension


produtos = [
    {'nome' : 'p1', 'preco': 10,},
    {'nome' : 'p2', 'preco': 11},
    {'nome' : 'p3', 'preco': 30},

]

novos_produtos = [
    {**produto,'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # if ternario
    for produto in produtos
]   

print(*novos_produtos, sep='\n')