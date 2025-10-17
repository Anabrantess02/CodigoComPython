class Carro: #inicilaizando a classe carro
    def __init__(self, modelo, marca, ano, potencia, cambio, preco): #definindo a função carro e seus atributos
        self.modelo = modelo #chamando os atributos
        self.marca = marca
        self.ano = ano
        self.potencia = potencia
        self.cambio = cambio
        self.preco = preco

    # Métodos para retornar cada atributo
    def get_modelo(self):
        return self.modelo

    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_potencia(self):
        return self.potencia

    def get_cambio(self):
        return self.cambio

    def get_preco(self):
        return self.preco

# Criando 3 instâncias de Carro
carro1 = Carro("Gol", "Volkswagen", 2020, 1.6, "Manual", 60000)
carro2 = Carro("Onix", "Chevrolet", 2021, 1.0, "Automático", 70000)
carro3 = Carro("Corolla", "Toyota", 2022, 2.0, "Automático", 120000)

# Testando os métodos
carros = [carro1, carro2, carro3]

for i, carro in enumerate(carros, 1):
    print(f"\nInformações do carro {i}:")
    print("Modelo:", carro.get_modelo())
    print("Marca:", carro.get_marca())
    print("Ano:", carro.get_ano())
    print("Potência:", carro.get_potencia())
    print("Câmbio:", carro.get_cambio())
    print("Preço:", carro.get_preco())