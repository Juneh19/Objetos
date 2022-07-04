class Conta:

    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {}, conta {}, é de {} reais.".format(self.__titular, self.__numero, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, origem, destino):
        origem.saque(valor)
        destino.deposito(valor)
