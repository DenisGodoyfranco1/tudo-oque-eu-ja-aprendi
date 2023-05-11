import os   


palavra_secrta = 'amor voce e muito especial para mim descupe por nao pensar em algo melhor'
letras_acertadas = ''
numeros_de_tentativas = 0
while True:
    

    letra_digitada = input('Digite apenas uma letra')
    numeros_de_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_digitada in palavra_secrta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secrta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += ('*')
    os.system('cls')
    print('palavra formado', palavra_formada)
    if palavra_formada == palavra_secrta:
        print('PARABENS VOCE GANHOU')
        print('a palavra secreta era', palavra_secrta)
        print(f'voce teve {numeros_de_tentativas} tentativas')
        letras_acertadas = ''
        numeros_de_tentativas = 0