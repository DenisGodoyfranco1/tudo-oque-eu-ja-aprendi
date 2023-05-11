# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))
# pass


lista = [
    (x,y) # da para colacar varia coisa aqui 
    for x in range(3)
    for y in range(3)
]
print(lista)

