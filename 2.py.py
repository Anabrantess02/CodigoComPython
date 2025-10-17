class Cliente:     #inicializando a classe
    def __init__(self, nome, cpf, endereco): #definindo a função e os atributos da função
        self.nome = nome      #chamando os atributos
        self.cpf = cpf
        self.endereco = endereco
class Conta_Corrente(Cliente):
    def __init__(self, nome, cpf, endereco, saldo_inicial=0):
        super().__init__(nome, cpf, endereco)
        self.__saldo = saldo_inicial  # saldo privado
    def depositar(self, valor): #função para depositar
     if valor > 0:
            self__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!") #mensagem
     else:
            print("Valor inválido para depósito.")
    def sacar(self, valor):
        if 0 valor = self__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    def consultar_saldo(self): #função para consultar saldo
        return self__saldo

    def consultar_info(self): #função para consultar informação
        return f"Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}" #retornando os tributos

    def alterar_info(self, nome=None, cpf=None, endereco=None): #função para alterar informação
        self.nome = nome #chamando os atributos
        self.cpf = cpf
        self.endereco = endereco
        print("Informações atualizadas com sucesso!")
        # Instância de teste
conta1 = Conta_Corrente("Ana Carolina", "12345678900", "Rua A, 123", 1000)

# Testando os métodos
conta1.consultar_info()        # Mostrar informações do cliente
conta1.consultar_saldo()       # Mostrar saldo inicial
conta1.depositar(500)          # Depositar R$500
conta1.consultar_saldo()       # Verificar saldo
conta1.sacar(200)              # Sacar R$200
conta1.consultar_saldo()       # Verificar saldo
conta1.sacar(2000)             # Tentar sacar valor maior que saldo
conta1.alterar_info(endereco="Rua B, 456")  # Alterar endereço
conta1.consultar_info()        # Conferir alterações