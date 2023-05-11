# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
      'Nome':'Denis',
     'Sobrenome':'Franco'
 }

# print(p1.get('Nome', 'nao existe')) # precisa nao exitir para fucionar 

# nome = p1.pop('Nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem('Sobrenome')
# print(ultima_chave)
# print(p1)

# p1.update({
#     'Nome': 'Novo Valor'

# })
# p1.update(Nome='novo valor', idade=30)
tupla = ('nom2e','Den2is'),('idade',30)
p1.update(tupla)
print(p1)
