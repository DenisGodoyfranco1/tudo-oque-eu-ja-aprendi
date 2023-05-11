"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
# quando precisar pricisamrnte um ultimo numero da conta de ponto flutuande usar import decimal(d)
numero_1 = decimal.Decimal (0.7)
numero_2 = decimal.Decimal (0.1)
conta = (numero_1 + numero_2)
print(conta
)
#ja se quiser a conta cerinha usando decimal colocar ele em str para dar certo
numero_1_str = decimal.Decimal ('0.7')
numero_2_str = decimal.Decimal ('0.1') 
numero_3 = numero_1_str + numero_2_str
print(numero_3)
print(f'{numero_3:.1f}'
)
print(f'{numero_3:.2f}'
)
print(round(numero_3,1
))
print(round(numero_3,2
))
