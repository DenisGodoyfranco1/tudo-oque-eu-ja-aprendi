#culculadora de juros compostos

while True:
    entrada = input('m(Montante) , c(Capital) j(Juros)')
    if entrada == 'm':
        c = float(input('Digite o capital --> '))
        i = float(input('Digite o juros --> '))
        n = float(input('Digite o tempo da aplicacao --> '))
        
        calculo_do_montante = c * (1 + i/100)**n
        print(f'O seu montante e = {calculo_do_montante:.4f}')
        break
    elif entrada == 'c':
        m = float(input('Digite o montante --> '))
        i = float(input('Digite o juros --> '))
        n = float(input('Digite o tempo da aplicacao --> '))
        
        calculo_do_montante_de_capital = (1 + i/100)**n
        resultado_final = (m/calculo_do_montante_de_capital)
        print(f'O seu Capital e = {resultado_final:.4f}')
        break
    elif entrada == 'j':
        m = float(input('Digite o montante --> '))
        c = float(input('Digite o capital --> '))
        n = float(input('Digite o tempo da aplicacao --> '))
        
        calculo_do_montante_com_capital = m/c 
        raiz = calculo_do_montante_com_capital ** (1/n)
        resultado_final = (raiz - 1) * 100

        print(calculo_do_montante_com_capital)
        
        print(f'O juro e = {resultado_final:.4f}')
        break



    else:
        print('ALGO DEU ERRADO')