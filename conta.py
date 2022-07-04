class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo = "001"

    def extrato(self):
        print("O saldo do titular {}, conta {}, é de {} reais.".format(self.__titular, self.__numero, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __permitido(self, valor_saque):
        valor_maximo = self.__saldo + self.__limite
        return valor_saque <= valor_maximo

    def saque(self, valor):
        if self.__permitido(valor):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite, pobretão.".format(valor))

    def tranferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo():
        return "001"
