class Conta:
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self,novoSaldo):
        self._saldo = novoSaldo

    def get_titular(self):
        return self._titular

    def set_titular(self,novoTitular):
        self._titular = novoTitular

conta1 = Conta("Jorge","2000")

print("O saldo da conta é:",conta1.get_saldo())
print("O titular da conta é:",conta1.get_titular())

conta1.set_saldo(300)
conta1.set_titular("Dida")

print("O novo titular da conta é:",conta1._titular)
print("O novo saldo da conta é:",conta1._saldo)

