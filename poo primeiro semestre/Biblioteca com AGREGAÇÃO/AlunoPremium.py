from Aluno import Aluno

class Alunovip(Aluno):
    def __init__(self, ra, nome, sobrenome, cpf, senha, tipo_assinatura, tempofidelidade):
        super().__init__(ra, nome, sobrenome, cpf)
        self._senha = senha
        self._tipo_assinatura = tipo_assinatura
        self._tempofidelidade = tempofidelidade

    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            teste = input("1 para verificar assinatura, 2 para ver seu tempo de fidelidade: \n")
            if teste == '1':
                  self.assinatura()
            else:
                  self.tempo()
                
            return True
    
        else:
            print("Acesso negado")
            return False
        
    def assinatura(self):
                print(f'Sua assinatura é {self._tipo_assinatura}')

    def tempo(self):
                print(f'Seu tempo de fidelidade é {self._tempofidelidade}')
                
                
                