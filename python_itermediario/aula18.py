#vamos aprender sobre kargs
# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)



# a, b = pessoa.values()
# print(a,b)

# (a1,a2),(b1,b2) = pessoa.items()
# print(a1)
# print(a2)
# print(b1)
# print(b2)

# for key, value in pessoa.items():
#     print(key,value)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_da_pessoa = {
    'idede' : 18,
    'altura' : 1.80,
}

pessoa_completa = {**pessoa,
**dados_da_pessoa,
'nome1' : 'Denis',
'sobrenome2' : 'franco',

}


def mostra_agumentos_nomeados(*args ,**kwargs):
    print('nao nomeados:',args)
    
    for chave,valor in kwargs.items():
        print(chave,valor)

mostra_agumentos_nomeados(1, 2, nome='joao', altura=1.80, idade=18)