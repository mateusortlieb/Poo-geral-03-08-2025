from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, cargo, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, cargo, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios
        
    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False
        
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00
        