class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def exibnome(self):
            print('O nome do pessoinha é {} \n'.format(self.nome))

    def exibidade(self):
            print('A idade do pessoinha é {} \n'.format(self.idade))

    def exibsalario(self):
            print('O salario do pessoinha é {} \n'.format(self.salario))


    