"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y , z):
    
    print(f'{x=} {y=} {z=}','|',f'{x} + {y} = {x + z + y}' )
# soma(1 , 2)
soma(y=2, x=1, z=4)
