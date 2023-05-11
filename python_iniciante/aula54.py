string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],]  # 2
#primeiro, b, c,*_,antipenultimo,ultimo = lista
#print(primeiro,antipenultimo, ultimo)

#for nome in lista:
#    print(nome,end='-') 


#ou da para fazer isso tambem
print(*lista[0])
# print(*tupla)
# print(*string)
# print(*salas, sep='\n')#para para ver como a sua lista foi montada 