#parte 3
try:
    print(1)
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('voce esta tentando dividir por Zero')
else:
    print('nao deu erro')
finally:
    print(123) # finally sempre vai ser excutado  
    