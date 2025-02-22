class contabancaria:
    def __init__ (self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def get_saldo(self):
        print(f'Saldo: {self.saldo}')
        return self.saldo

conta1 = contabancaria(1000)
conta1.sacar(700)
conta1.depositar(1200)

print(conta1.get_saldo())

           