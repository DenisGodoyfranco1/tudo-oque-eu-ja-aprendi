"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['denis', 'lua', ],  # 0
    # 0
    ['pedro', ],  # 1
    # 0       1       2
    ['maicon', 'João', 'ferdinando',] #(0,10,20,30,40)],  # 2
]
for sala in salas:
    for aluno in sala:
        print(aluno)