""" 
repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
"""
condicao = True

while condicao:
    nome = input('qual é seu nome')
    print(f'seu nome é {nome}')
    if nome == 'sair':
        break
print('acabou')
