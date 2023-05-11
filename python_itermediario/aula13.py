# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]



print(perguntas[0]['Pergunta'])
total = 0 


for abc in 'A)','B)','C)','D)':
        
    perguntas_1 = perguntas[0]['Opções'][total] 
    perguntas[0]['Opções'][0]
    print(abc,perguntas_1)
    total += 1
    

respota = input('Qual a resposta correta?  :')
if respota == 'c':
    print('ACERTOU👍')
    
elif respota == '4':
    print('ACERTOU👍')
    
else:
    print('ERROU❌')

print(perguntas[1]['Pergunta'])
total = 0 


for abc in 'A)','B)','C)','D)':
        
    perguntas_1 = perguntas[1]['Opções'][total] 
    perguntas[1]['Opções'][1]
    print(abc,perguntas_1)
    total += 1
    

respota = input('Qual a resposta correta?  :')
if respota == 'a':
    print('ACERTOU👍')
    
elif respota == '25':
    print('ACERTOU👍')
    

else:
    print('ERROU❌')


print(perguntas[2]['Pergunta'])
total = 0 


for abc in 'A)','B)','C)','D)':
        
    perguntas_1 = perguntas[2]['Opções'][total] 
    perguntas[2]['Opções'][2]
    print(abc,perguntas_1)
    total += 1
    

respota = input('Qual a resposta correta?  :')
if respota == 'b':
    print('ACERTOU👍')
     
elif respota == '5':
    print('ACERTOU👍')
     
    
else:
    print('ERROU❌')
    
    