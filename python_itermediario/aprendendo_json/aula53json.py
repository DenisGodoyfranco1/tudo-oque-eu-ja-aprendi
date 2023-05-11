import json
pessoas = [
{
    "nome": "denis",
    "lastname": "franco", 
    "age": 17,
    "adrsses": [
        {"line1": "Rua salomao muigues nasser"},{"line1":1055}
]
},
{"nome": "lua","lastname": "tofolo","age": 16},
{"nome": "maicon","lastname": "rodrigues","age": 17}
]

with open('aula55.json', 'w') as arquivo:
    json.dump(pessoas,arquivo, indent= 2)
     