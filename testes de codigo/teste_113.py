# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
    
# soma_1 = multiplicar(1,2,3,4,5,6,7,8,9,10)
# print(soma_1)

# segundo exercicio par ou impar

def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'o numero {numero}-é par'
    #nesse caso nao precisa de else por que ele fica redundante 
    return f'o numero {numero}-é impar'
        
print(impar_par(10))
print(impar_par(5))
print(impar_par(11))
print(impar_par(12))
print(impar_par(15))



