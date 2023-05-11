class Pessoa:
    ano_atual = 2023
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('maicon',17)
p2 = Pessoa('denis',18)
p3 = Pessoa('lua',17)

print(p1.__dict__)
print(vars(p1))

     