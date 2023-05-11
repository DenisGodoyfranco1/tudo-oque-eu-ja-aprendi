#cpf 

cpf_do_cliente = '10788460900' \
    .replace(' ','')\
    .replace('.','')\
    .replace('-','')

nove_digitos = cpf_do_cliente[:9]
contador = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador
    contador -= 1

digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
#calcular o segundo digito e a mesmo coisa mais tem que incluir o primeiro digitodd 
dez_digitos = cpf_do_cliente[:10]
contador_2 = 11
resultado_2 = 0

for digito_da_segundo_conta in dez_digitos:
    resultado_2 += int(digito_da_segundo_conta) * contador_2  
    contador_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2= digito_2 if digito_2 <=9 else 0


#como validar um cpf :
cpf_da_conta = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_da_conta == cpf_do_cliente:
    print(f'{cpf_do_cliente} e valido')
else:
    print('cpf invalido')



#cpf outra maneira de fazer com import re
# import re
# entrada = input('digite um cpf :')
# cpf_do_cliente = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )
# primeiro_caractere_entrada = entrada[0]
# primeiro_caractere_entrada_repetido = primeiro_caractere_entrada * len(entrada)

# if entrada == primeiro_caractere_entrada_repetido:
#     False
#     print('por favor nao repita numeros')




    
# nove_digitos = cpf_do_cliente[:9]
# contador = 10

# resultado = 0
# for digito in nove_digitos:
#     resultado += int(digito) * contador
#     contador -= 1

# digito_1 = (resultado * 10) % 11
# digito_1 = digito_1 if digito_1 <=9 else 0
# #calcular o segundo digito e a mesmo coisa mais tem que incluir o primeiro digitodd 
# dez_digitos = cpf_do_cliente[:10]
# contador_2 = 11
# resultado_2 = 0

# for digito_da_segundo_conta in dez_digitos:
#     resultado_2 += int(digito_da_segundo_conta) * contador_2  
#     contador_2 -= 1
# digito_2 = (resultado_2 * 10) % 11
# digito_2= digito_2 if digito_2 <=9 else 0


# #como validar um cpf :
# cpf_da_conta = f'{nove_digitos}{digito_1}{digito_2}'
# if cpf_da_conta == cpf_do_cliente:
#     print(f'{cpf_do_cliente} e valido')
# else:
#     print('cpf invalido')

# import re
# import sys

# entrada = input('CPF [746.824.890-70]: ')
# cpf_enviado_usuario = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )

# entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_e_sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')