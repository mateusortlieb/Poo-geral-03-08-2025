from historico import Historico

class Livro:
    def __init__(self, ISBN, nome, autor, editora, status, ano, pessoa):
        self._isbn = ISBN
        self._nome = nome
        self._autor = autor
        self._editora = editora
        self._status = status
        self._ano = ano
        self._pessoa = pessoa
        self.historico = Historico()

    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, ISBN):
        self._isbn = ISBN

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

    def get_autor(self):
        return self._autor
    
    def set_autor(self, autor):
        self._autor = autor

    def get_editora(self):
        return self._editora
    
    def set_editora(self, editora):
        self._editora = editora

    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status

    def get_ano(self):
        return self._ano
    
    def set_ano(self, ano):
        self._ano = ano

    def get_pessoa(self):
        return self._pessoa
    
    def set_pessoa(self, pessoa):
        self._pessoa = pessoa

    def emprestar(self, pessoa):
        self._status = 'Indisponível'
        self._pessoa = pessoa
        print('O livro foi emprestado para {} '.format(self._pessoa._nome))
        self.historico.alteracao.append('Emprestimo de {} feito para {} na data {}'.format(self._nome, self._pessoa._nome, self.historico.data_mudança_status))

    def devolver(self):
        self._status = 'Disponível'
        self._pessoa = 'Biblioteca'
        print('O livro foi devolvido para a biblioteca')
        self.historico.alteracao.append('{} foi devolvido para a biblioteca. '.format(self._nome))

    def stat(self):
        print('O status atual do livro é {}'.format(self._status))
        self.historico.alteracao.append('O {} perguntou o status atual de {} '.format(self._pessoa, self._pessoa._nome))