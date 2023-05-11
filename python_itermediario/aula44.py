
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

def zipper(l1,l2):
    intervalo_maximo = min(len(l1),len(l2))
    return [
        (l1[i] + l2[i]) for i in range(intervalo_maximo)
    ]
        

print(zipper(lista_a,lista_b))

print(list(zip(lista_a , lista_b)))