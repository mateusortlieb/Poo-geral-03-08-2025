from livro import Livro
from Aluno import Aluno

aluno1 = Aluno('239', 'Mateus', 'Ortlieb', '11023976951')
livro1 = Livro('123', 'mentiras', 'eu', 'eutbm', aluno1, '2023', 'Bibioteca')
aluno2 = Aluno('434', 'Cesco', 'Fransce', '29496846582')
livro2 = Livro('555', 'falcatruas', 'my', 'aqueles', aluno2, '2025', 'Bibioteca')

print(f'O {livro1.nome} esta atualmente com {livro1.status.nome}')
print(f'O {livro2.nome} esta atualmente com {livro2.status.nome}')