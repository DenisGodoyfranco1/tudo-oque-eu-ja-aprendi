''' 
operadores de atribuicao
'''
contador = 0

while contador <+ 100:
    contador += 1
    if contador == 10:
        print('nao vai mostras o 10')
        continue
    
    if contador >= 50 and contador <=70:
        print('nao vai mostras a sequencia que eu colocar') 
        continue

    print(contador)

    if contador == 100:
        print('isso e tudo pessoal')
        break
