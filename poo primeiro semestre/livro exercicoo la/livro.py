class Livro:
    def __init__(self, ISBN, nome, autor, editora, status, ano, Patual):
        self.isbn = ISBN
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.status = status
        self.ano = ano
        self.atual = Patual

    def emprestar(self, pessoa):
        self.status = 'Indisponível'
        self.atual = pessoa
        print('O livro foi emprestado para {} '.format(self.pessoa))

    def devolver(self):
        self.satus = 'Disponível'
        self.atual = 'Biblioteca'
        print('O livro foi devolvido para a biblioteca')

    def stat(self):
        print('O status atual do livro é {}'.format(self.status))