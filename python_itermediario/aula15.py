# exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite uma letra : ')
    letras.add(letra)
    print(letra)

    if 'd' in letras :
        print('PARABENS VOCE ACHOU A LETRA')
        break
    print(letras)