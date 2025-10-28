from random import randint, choice
from especie import *


if __name__ == "__main__":
    print("Simulação de evolução de golfinhos \U0001F42C")

    tamanhopop = int(input("Quantos golfinhos na população inicial? "))
    geracoes = int(input("Quantas gerações você quer simular? "))
    populacao = [criarindividuo() for i in range(tamanhopop)]

    for i in range(1, geracoes + 1):
        print(f"\n Geração {i}")
        for i in populacao:
            print(f"{i.nome} ({i.sexo}) - Velocidade:{i.velocidade} Inteligência:{i.inteligencia} Sociabilidade:{i.sociabilidade}")

        maisapto = populacao[0]
        for golfinho in populacao:
            if golfinho.fitness() > maisapto.fitness():
                maisapto = golfinho

        print(f"\n Mais apto: {maisapto.nome} com fitness {maisapto.fitness():.2f}")


        novageracao = []
        for i in range(0, len(populacao) - 1):
            pai = populacao[i]
            mae = populacao[i + 1]
            filho = reproduzir(pai, mae)
            if filho.fitness() >= maisapto.fitness() * 0.7:
                novageracao.append(filho)

        if not novageracao:
            novageracao = [criarindividuo() for i in range(tamanhopop)]

        populacao = novageracao

    print("\nSimulação finalizada! \U0001F30A")
