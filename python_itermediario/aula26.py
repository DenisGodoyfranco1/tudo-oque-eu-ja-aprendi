# generator exepression,
import sys
interable = ['Eu','Denis', '__iter__']
iterator = interable.__iter__()# tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
generator = (n for n in range(10000))
lista = [n for n in range(10000)]
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
#mosta a valor guardado na menoria do seu computador

for n in generator:
    print(n)
# Aqui vai mostra a valor do generator um de cada fez para voce ate o 10000 ou ate 1000000

