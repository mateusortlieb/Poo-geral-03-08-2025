class Aluno:
    def __init__(self, ra, nome, sobrenome, cpf):
        self._ra = ra
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    def get_ra(self):
        return self._ra
    
    def set_ra(self, ra):
        self._ra = ra

    def get_nome(self):
        return self._nome
    
    def set_ra(self, nome):
        self._nome = nome

    def get_sobrenome(self):
        return self._sobrenome
    
    def set_ra(self, sobrenome):
        self._sobrenome = sobrenome
    
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf