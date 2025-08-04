from historico import Historico

class Livro:
    def __init__(self, ISBN, nome, autor, editora, status, ano, pessoa):
        self.isbn = ISBN
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.status = status
        self.ano = ano
        self.pessoa = pessoa
        self.historico = Historico()

    def emprestar(self, pessoa):
        self.status = 'Indisponível'
        self.pessoa = pessoa
        print('O livro foi emprestado para {} '.format(self.pessoa.nome))
        self.historico.alteracao.append('Emprestimo de {} feito para {} na data {}'.format(self.nome, self.pessoa.nome, self.historico.data_mudança_status))

    def devolver(self):
        self.status = 'Disponível'
        self.pessoa = 'Biblioteca'
        print('O livro foi devolvido para a biblioteca')
        self.historico.alteracao.append('{} foi devolvido para a biblioteca. '.format(self.nome))

    def stat(self):
        print('O status atual do livro é {}'.format(self.status))
        self.historico.alteracao.append('O {} perguntou o status atual de {} '.format(self.pessoa, self.pessoa.nome))