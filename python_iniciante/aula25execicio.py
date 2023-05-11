nome = input('Digite seu nome  ')
idade = input('Me fala a sua idade  ')

if nome and idade:
    print(f'seu nome e {nome}')
    print(f'sua idade e {idade}')
    print(nome[::-1])
    if ' ' in nome:
        print(f'seu nome {nome} contem espacos')
    else:
        print(f'seu nome {nome} nao contem espacos')

    print('Teu nome tem ',len(nome),'letras')
    print('a primeira letra do seu nome e',nome[0:1])
    print('a ultima letra do seu nome e',nome[-1:])
else:
     print('"Desculpe voce nao colocou todas as imformacoes"')
print (f'o teu nome e {nome} e sua idade e {idade}')


#Do professor
''' nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
    
    '''