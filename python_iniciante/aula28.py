"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_1 = input('Digite um número para eu saber se é par ou impar: ')
int_numero_1 = int(numero_1)
conta = (int(int_numero_1 % 2))

if  conta > 0:
    print('impar')
else:
    print('par')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = (int(input('que horas sao  :')))
bom_dia = (1,2,3,4,5,6,7,8,9,10,11,12)
boa_tarde = (13,14,15,16,17,18)
boa_noite = (19,20,21,22,23)

if horario in bom_dia:
    print('bom dia')
if horario in boa_tarde:
    print('boa tarde')
if horario in boa_noite:
   print('boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
n = input('qual é seu nome  :')

nome = (len(n))

if nome <= 4:
    print('Seu nome é curto')
if nome <= 6:
    print('seu nome e medio')
if nome >= 7:
    print('seu nome e muito grande')