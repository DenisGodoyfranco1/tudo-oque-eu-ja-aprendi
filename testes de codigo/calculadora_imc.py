
nome = input('Qual seu nome -->')
altura = float(input('Qual sua altura -->'))
peso = float(input('Qual o seu peso -->'))
imc = peso / altura ** 2
ganhar = peso 
perder = peso

print(f'o seu imc {nome} e --> {imc:.2f}')

if imc <= 18:
    print('Voce esta em estado de magreza')
elif imc <= 25:
    print('Voce esta normal')
elif imc <= 30:
    print('Voce esta obsedade')
else:
    print('Voce esta obsedade extrema')


