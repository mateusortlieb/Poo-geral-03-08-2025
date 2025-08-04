from conta import Conta
from cliente import Cliente

cl1 = Cliente('Mateus', 'Ortlieb', '11023976951')
cl2 = Cliente('Cesco', 'fofucho', '13043974839')
c1 = Conta('111-4', cl1, 333, 1000)
c2 = Conta('222-8', cl2, 666, 2000)

print(c1.saldo)
