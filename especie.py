from random import randint, choice

class Golfinho:
    def __init__(self, nome, sexo, velocidade, inteligencia, sociabilidade):
        self.nome = nome
        self.sexo = sexo
        self.velocidade = velocidade
        self.inteligencia = inteligencia
        self.sociabilidade = sociabilidade
        self.geracoesvivas = 1

    def fitness(self):
        return (self.velocidade + self.inteligencia + self.sociabilidade) / 3


def criarindividuo():
    nomes = ["Boto cor de Rosa", "Commerson", "Rotador", "Orca"]
    nome = choice(nomes)
    sexo = choice(["M", "F"])
    velocidade = randint(1, 100)
    inteligencia = randint(1, 100)
    sociabilidade = randint(1, 100)
    return Golfinho(nome, sexo, velocidade, inteligencia, sociabilidade)


def reproduzir(pai, mae):
    nomes = ["Boto cor de Rosa", "Commerson", "Rotador", "Orca"]
    nome = choice(nomes)
    sexo = choice(["M", "F"])
    velocidade = (pai.velocidade + mae.velocidade) // 2
    inteligencia = (pai.inteligencia + mae.inteligencia) // 2
    sociabilidade = (pai.sociabilidade + mae.sociabilidade) // 2
    return Golfinho(nome, sexo, velocidade, inteligencia, sociabilidade)
