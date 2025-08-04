from historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (self._saldo < 0):
            print('Saida não pode ser negativa')
        else:
            self._saldo = saldo

    
    def depositar(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("Deposito de {}".format(valor))

    def sacar(self, valor):
        # self.saldo -= valor
        if(self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True

    def extrato(self):
        print("Numero {} \nsaldo {}".format(self._numero, self._saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self._saldo))

    def transferencia(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
             return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferencia de {} para conta de {}".format(valor, destino._numero))
            return True

    
    