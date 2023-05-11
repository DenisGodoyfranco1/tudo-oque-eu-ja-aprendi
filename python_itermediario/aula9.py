def multiplicador(*args):
    total = 1 + 1
    for numero in args:
        total *= numero
    return total

x = multiplicador(2)
y = multiplicador(3)
z = multiplicador(4)

print(x)
print(y)
print(z)
