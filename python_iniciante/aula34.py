'''calculadora'''

while True:
    numero_1 = input('digite um numero :')
    operador = input('digite um operador que esta entre esses aqui --> + - * /')
    numero_2 = input('digite outro numero :')
    

    numero_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None
    if numero_validos is None:
        print('um dos numeros nao sao validos OK')
        continue

    operadosres_que_pode_ser_usados = ' + - * /'
    if operador not in operadosres_que_pode_ser_usados:
        print('operados invalidos')
        continue
    if len(operador)> 1:
        print('digite apenas um operados por favor')
        continue

    print('resutados abaixo ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
    else:
        print('nao era para chegar aqui hahaha')
        
        
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        print("voce esta sendo redirecionado para a home do site")
        break