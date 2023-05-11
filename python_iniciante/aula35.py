frase = 'o python e uma linguagem de programacao multiparadigima' \
    'python foi criado por guido van rossum'.lower()

#print(frase)

#qual_letra = input('O que voce quer procurar nessa frase:  ')
#print(frase.count(qual_letra))

i = 0
qtd_apareceu_mais_vezes = 0
letra_q_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': 
        i += 1
        continue


    qtd_atual = frase.count(letra_atual)
    if qtd_apareceu_mais_vezes < qtd_atual :
        qtd_apareceu_mais_vezes = qtd_atual
        letra_q_apareceu_mais_vezes = letra_atual
    i += 1

print('a letra que mais apareceu foi'
    f'{letra_q_apareceu_mais_vezes}que apereceu'
    f'{qtd_apareceu_mais_vezes}X'
    )
