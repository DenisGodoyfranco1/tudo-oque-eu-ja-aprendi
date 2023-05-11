"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2    3   4
lista =[10 , 20 , 30 ,40 , 50] 
#del lista[0]
# lista.clear()
while True:
    anotacoes_mercado = int(input('adicionar a lista'))
    lista.pop(anotacoes_mercado)
    print(lista)