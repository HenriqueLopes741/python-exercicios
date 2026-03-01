class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular      # atributo
        self.saldo = saldo_inicial  # atributo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo}")


    
conta1 = ContaBancaria("Henrique", 100)
conta2 = ContaBancaria("Maria", 50)

conta1.depositar(50)
conta1.sacar(30)
conta1.mostrar_saldo()

print("-----")

conta2.sacar(100)
conta2.mostrar_saldo()