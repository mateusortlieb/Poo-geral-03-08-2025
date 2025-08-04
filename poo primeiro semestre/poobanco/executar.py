from conta import Conta

c1 = Conta('123-4', 'mameuusuuuss', 333, 1000)
c2 = Conta('323-4', 'mam', 733, 2000)
c3 = Conta('333-4', 'peni', 343, 1500)
# c1 é um atributo de referencia para um objeto, para que isso ocorra no python são acionados de forma transparente os métodos magicos, __new__ e __init__ (responsavei s por construir e iniciar objetos)
