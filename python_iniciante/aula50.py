"""fazer uma lista de mercado para uma usuario
"""
#como eu vou comercar essa lista como ela tem que inserir apagar e listar vamos comecar com as fucoes do input
lista = []

while True:
    entrada = input('[i]nserir [a]pagar [l]istar :')
    if entrada == 'i':
        anotacoes_mercado = input('o que voce quer adicionar na sua lista :')
        lista.insert(0,anotacoes_mercado)

    elif entrada == 'a':
        if entrada == 'a':
            try:  
                anotacoes_mercado = int(input('o que voce quer apagar na sua lista :')) 
                lista.pop(anotacoes_mercado)
                indices = len(lista)
            except ValueError:
                print('voce nao pode colocar isso aqui porfavor coloque um numero')
            except IndexError:
                print('esse numero ainda nao exite')
           
                
    elif entrada == 'l':
        indices = range(len(lista))
        for indice in indices:
             print(indice,lista[indice])


    else:
        print('algo deu errado')

