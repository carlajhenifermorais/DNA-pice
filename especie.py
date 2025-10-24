class Golfinho:
    def __init__(self, nome, sexo, velocidade, inteligencia, sociabilidade):
        self.nome = nome
        self.sexo = sexo
        self.velocidade = velocidade
        self.inteligencia = inteligencia
        self.sociabilidade = sociabilidade
        self.geracoes_vivas = 1

    def fitness(self):
        return (0.4 * self.velocidade + 0.3 * self.inteligencia + 0.3 * self.sociabilidade)

    def criarindividuo():
        nomes = ["Flippy", "Luna", "Splash", "Coral", "Bubbles"]
        nome = choice(nomes)
        sexo = choice(["M", "F"])
        velocidade = randint(1, 100)
        inteligencia = randint(1, 100)
        sociabilidade = randint(1, 100)
        return Golfinho(nome, sexo, velocidade, inteligencia, sociabilidade)

    def reproduzir(pai, mae):
        nome = choice(["Wave", "Blue", "Sunny", "Echo"])
        sexo = choice(["M", "F"])
        velocidade = max(pai.velocidade, mae.velocidade)
        inteligencia = max(pai.inteligencia, mae.inteligencia)
        sociabilidade = max(pai.sociabilidade, mae.sociabilidade)
        filho = Golfinho(nome, sexo, velocidade, inteligencia, sociabilidade)
        return mutacao(filho)

    def mutacao(individuo):
        if randint(1, 10) == 1:
            x = randint(1, 3)
            if x == 1:
                individuo.velocidade = randint(1, 100)
            elif n == 2:
                individuo.inteligencia = randint(1, 100)
            else:
                individuo.sociabilidade = randint(1, 100)
        return individuo
