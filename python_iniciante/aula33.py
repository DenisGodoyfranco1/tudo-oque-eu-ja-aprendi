"""
exercicio

"""

nome = "denis godoy franco"
tamanho_do_nome = len(nome)
print(nome)
print(f'{tamanho_do_nome} letras')
indice = 0 
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    
    novo_nome += f'*{letra}'
    indice += 1

print(f'{novo_nome}')

    