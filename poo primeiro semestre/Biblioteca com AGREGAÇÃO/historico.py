import datetime

class Historico:
    def __init__(self):
        self.data_mudança_status = datetime.datetime.today()
        self.alteracao = []
    
    def imprime(self):
        print('Data de alteração: {} '.format(self.alteracao))
        print('Alterações: ')
        for t in self.alteracao:
            print("-", t)