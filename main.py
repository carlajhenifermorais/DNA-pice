from random import randint, choice
from especie import *

VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

if __name__ == "__main__":
    print("Simulação de evolução de golfinhos \U0001F42C")

    qtdpop = int(input("Quantos golfinhos na população inicial? "))
    qtdnova = int(input("Quantos golfinhos terão na nova geração? "))
    geracoes = int(input("Quantas gerações quer simular? "))
    populacao = [criarindividuo() for i in range(qtdpop)]

    for i in range(1, geracoes + 1):
        print(f"\n GERAÇÃO {i}")
        for golfinho in populacao:
            print(f"{golfinho.nome} ({golfinho.sexo}) - Velocidade:{golfinho.velocidade} Inteligencia:{golfinho.inteligencia} Sociabilidade:{golfinho.sociabilidade} | Gerações vivas: {golfinho.geracoesvivas}")

        maisapto = populacao[0]
        for golfinho in populacao:
            if golfinho.fitness() > maisapto.fitness():
                maisapto = golfinho

        print(f"\n Mais apto: {maisapto.nome} (Fitness: {maisapto.fitness():.2f})")

        novapop = []
        for j in range(qtdnova):
            pai = choice(populacao)
            mae = choice(populacao)
            filho = reproduzir(pai, mae)

            print(f"\n Filho {j+1}:")

            if filho.velocidade > maisapto.velocidade:
                print(f"Velocidade: {VERDE}{filho.velocidade} (ganhou){RESET}")
            elif filho.velocidade < maisapto.velocidade:
                print(f"Velocidade: {VERMELHO}{filho.velocidade} (perdeu){RESET}")
            else:
                print(f"Velocidade: {filho.velocidade} (igual)")

            if filho.inteligencia > maisapto.inteligencia:
                print(f"Inteligência: {VERDE}{filho.inteligencia} (ganhou){RESET}")
            elif filho.inteligencia < maisapto.inteligencia:
                print(f"Inteligência: {VERMELHO}{filho.inteligencia} (perdeu){RESET}")
            else:
                print(f"Inteligência: {filho.inteligencia} (igual)")

            if filho.sociabilidade > maisapto.sociabilidade:
                print(f"Sociabilidade: {VERDE}{filho.sociabilidade} (ganhou){RESET}")
            elif filho.sociabilidade < maisapto.sociabilidade:
                print(f"Sociabilidade: {VERMELHO}{filho.sociabilidade} (perdeu){RESET}")
            else:
                print(f"Sociabilidade: {filho.sociabilidade} (igual)")

            novapop.append(filho)

        for golfinho in populacao:
            golfinho.geracoesvivas += 1

        populacao = novapop

    print("\nSimulação finalizada! \U0001F30A")
