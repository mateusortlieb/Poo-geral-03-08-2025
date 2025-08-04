class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self._nome = nome
        self._cpf = cpf
        self._cargo = cargo
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
            self._nome = nome

    def get_bonificacao(self):
         return self._salario * 0.10
