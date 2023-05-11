# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC , abstractmethod

class Noificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mesagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NoificacaoEmail(Noificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando:',self.mesagem)
        return True

class NoificacaoSms(Noificacao):
    def enviar(self) -> bool:
        print('Sms: enviando:',self.mesagem)
        return False


def notificar(notificar: Noificacao):
    notificao_enviada = notificar.enviar()

    if notificao_enviada:
        print('notificacao enviada')
    else:
        print('notificacao nao enviada')

notificacao_email = NoificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NoificacaoSms('testando sms')
notificar(notificacao_sms)