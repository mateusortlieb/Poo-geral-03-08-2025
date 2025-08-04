from historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Deposito de {}".format(valor))

    def sacar(self, valor):
        # self.saldo -= valor
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True

    def extrato(self):
        print("Numero {} \nsaldo {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transferencia(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
             return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferencia de {} para conta de {}".format(valor, destino.numero))
            return True

    