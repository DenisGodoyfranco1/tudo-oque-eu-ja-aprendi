# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...

class OutrosError(Exception):
    ...


def levantar():
    exeption_ = MeuError('A','b','c')
    exeption_.add_note('olha minha nota')
    exeption_.add_note('Isso esta errado')
    raise exeption_

try:

    levantar()
except MeuError as error:
    print(error.args)
    print(error.__class__.__name__)
    exeption_ = OutrosError('vou lancar de novo')
    exeption_.__notes__ += error.__notes__.copy()
    exeption_.add_note('Mais um nota')
    raise exeption_ from error