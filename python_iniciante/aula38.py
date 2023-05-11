"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#texto = 'denis'.__iter__   
#texto = iter('denis')
 
 #for letra in texto
'''
texto = 'denis'# iterator
iteratador = iter(texto) #iterator

while True:
    try:
        letra =next(iteratador)
        print(letra)
    except StopIteration:
            break
'''
texto = 'denis'
for letra in texto:
    print(letra)