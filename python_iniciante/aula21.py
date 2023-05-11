#Operadores in not in
#strigns sao interaveis
# D e n i s 
# 0 1 2 3 4 
#nome = 'Denis'
#print(nome [2])
#print('nis' in nome)
#print('D' in nome)
#print('h' not in nome)
#print('l' not in nome)
#print('c' not in nome)
nome =input('digete seu nome meu caro amigo  ')
encontrar =input('O que voce deseja encontrar jovem????  ')

if encontrar in nome:
    print(f'{encontrar}  esta do {nome}')
else:
    print(f'{encontrar}  nao esta no {nome}')