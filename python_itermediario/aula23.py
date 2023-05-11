#Dictionary Comprehension e Set Comprehension

produto = {
'nome' : 'caneta azul',
'preco': 2.50,
'categoria' : 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
        
}
# print(dc)

lista = [
    ('a','valor' 'a'),
    ('b','valor' 'a'),
    ('c','valor' 'a'),
]

# print(dict(lista))

#set conprehension

s1 = {i for i in range(10)}
print(s1)