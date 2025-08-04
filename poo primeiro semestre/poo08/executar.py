from conta import Conta
from cliente import Cliente
from funcionario import Funcionario
from gerente import Gerente

cl1 = Cliente('Mateus', 'Ortlieb', '11023976951')
cl2 = Cliente('Cesco', 'fofucho', '13043974839')
c1 = Conta('111-4', cl1, 333, 1000)
c2 = Conta('222-8', cl2, 666, 2000)
gerente = Gerente('mameuuuuussss', '292929', 'gerente', 50.000 ,'123', 40)


print(gerente.get_bonificacao())
gerente.autentica('123')
