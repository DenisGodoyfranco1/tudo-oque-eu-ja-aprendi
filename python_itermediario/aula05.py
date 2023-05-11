"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    

soma1_2_3 = soma(1,2,3)
# print(soma1_2_3)
soma4_5_6 = soma(4,5,6)
# print(soma4_5_6)
tupla = 1,2,3,4,56,67,78,14
outro_soma = soma(*tupla)
print(outro_soma)
print(sum(tupla)) 