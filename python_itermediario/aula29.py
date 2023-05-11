#try, except, else e finally


try:
    a = 18
    b = 0
    print('linha1')
    c = a / b
    print('linha2')
    # do erro ele ja vai para o except
except ZeroDivisionError:
    print('voce dividio por zero faca de novo')
except NameError as error:
    print('nome:', error)
    print('nome b nao esta definido')
except Exception:#maior excecao de todos except
    print('ERRO DESCONHECIDO')