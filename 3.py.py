class Planeta: #inicializando a classe planeta
    def __init__(self, nome, raio_equatorial, distancia_do_sol, composicao): #definindo a função
        self.nome = nome
        self.raio_equatorial = raio_equatorial  # em km
        self.distancia_do_sol = distancia_do_sol  # em milhões de km
        self.composicao = composicao  # "Rochoso" ou "Gasoso"
    def apresentar(self):
        print(f"Planeta: {self.nome}")
        print(f"Raio equatorial: {self.raio_equatorial} km")
        print(f"Distância do Sol: {self.distancia_do_sol} milhões de km")
        print(f"Composição: {self.composicao}")
        print("---------------------------")
    