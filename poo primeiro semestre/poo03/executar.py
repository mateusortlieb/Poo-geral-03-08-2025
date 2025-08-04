from conta import Conta

c1 = Conta('111-4', 'mameuusuuuss', 333, 1000)
c2 = Conta('222-4', 'mam', 733, 2000)
c3 = Conta('333-4', 'peni', 343, 1500)

print(c1.saldo)
print(c2.saldo)
c2.transferencia(c1, 300)
print(c1.saldo)
print(c2.saldo)