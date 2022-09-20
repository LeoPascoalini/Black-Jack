import math
import random


class Cartas:
    def __init__(self, naipe, figura, valor):
        self.naipe = naipe
        self.figura = figura
        self.valor = valor

    numeroDeBaralhos = 1
    maxCartasMostradas = 10
    baralho = []
    maoDoDealer = []
    mao = []
    resultMao = 0

    naipes = ["♦", "♠", "♥", "♣"]
    figuras = ["A ", "2 ", "3 ", "4 ", "5 ", "6 ",
               "7 ", "8 ", "9 ", "10", "Q ", "J ", "K "]
    valores = {"A ": 1, "2 ": 2, "3 ": 3, "4 ": 4, "5 ": 5, "6 ": 6,
               "7 ": 7, "8 ": 8, "9 ": 9, "10": 10, "Q ": 10, "J ": 10, "K ": 10}

    @classmethod
    def addBaralho(cls, numero):
        for i in range(numero):
            for naipe in cls.naipes:
                for figura in cls.figuras:
                    cls.baralho.append(
                        Cartas(naipe, figura, cls.valores[figura]))

    @classmethod
    def distribuir(cls, numero):
        # TODO: adicionar parametro do dealer para ser possivel distribuir cartas para ele
        for i in range(numero):
            x = math.ceil(random.random() * len(cls.baralho)) - 1
            cls.mao.append(cls.baralho[x])
            cls.baralho.pop(x)

    @classmethod
    def mostrar(cls, dealerTurn=False):
        """Funcao que mostra as cartas de uma mao.\n
        Caso o dealerTurn (por padrao False) for setado para True, entao mostra as cartas da mao do dealer."""
        mao = cls.maoDoDealer if dealerTurn else cls.mao
        if dealerTurn:
            print("______________"*cls.maxCartasMostradas +
                  "\n\n" + "              "*(cls.maxCartasMostradas//2-1) + "Mão do dealer")

        linhas = len(mao)//cls.maxCartasMostradas
        linhas += 0 if len(mao) % cls.maxCartasMostradas == 0 else 1
        for j in range(linhas):
            final = len(mao) if (
                j+1) * cls.maxCartasMostradas > len(mao) else (j+1)*cls.maxCartasMostradas

            inicio = j*cls.maxCartasMostradas

            print(" _______      "*(final-inicio))

            for i in range(inicio, final):
                print(f"|{mao[i].naipe}      |", end="")
                print("     ", end="")

            print("\n"+"|       |     "*(final-inicio))

            for i in range(inicio, final):
                print(f"|   {mao[i].figura}  |", end="")
                print("     ", end="")

            print("\n"+"|       |     "*(final-inicio))

            for i in range(inicio, final):
                print(f"|______{mao[i].naipe}|", end="")
                print("     ", end="")

            print("")
        print("")
        if not dealerTurn:
            print("Carta do dealer:")
            print(
                f" _______ \n|{cls.maoDoDealer[0].naipe}      |\n|       |\n|   {cls.maoDoDealer[0].figura}  |\n|       |\n|______{cls.maoDoDealer[0].naipeD}|\n")

    @classmethod
    def somar(cls):
        # TODO: calculo do As
        Cartas.resultMao = 0
        for i in range(len(cls.mao)):
            Cartas.resultMao = cls.mao[i].valor + Cartas.resultMao
        print(f"A soma de suas cartas são: {Cartas.resultMao}")
        print("Desce mais uma ou Para?")

    @classmethod
    def decidir(cls, resp):
        match resp:
            case "Desce":
                Cartas.distribuir(1)
                Cartas.mostrar()
                Cartas.somar()
                return True
            case "Para":
                print(f"Você parou com: {Cartas.resultMao}")
                print("Aguardando o resultado do dealer...")
                return False
            case "Separa":
                pass
                # TODO: Implementar o split
            case _:
                print("Comando Incorreto")
