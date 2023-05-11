#primeiro ex bem facil
def soma(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
soma_1 = soma(1,2,3,4,5,6,7,8,9,10)
print(soma_1)


#segundo segunta tentativa
def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'o seu numero é {numero}-par'
    return f'o seu numero é {numero}-impar'

print(impar_par(10))
print(impar_par(15))
print(impar_par(20))
print(impar_par(12))
print(impar_par(14))
print(impar_par(18))