import math
import random


class Cartas:
    def __init__(self, naipe, figura, valor):
        self.naipe = naipe
        self.figura = figura
        self.valor = valor

    maxCartasMostradas = 10
    baralho = []
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
        for i in range(numero):
            x = math.ceil(random.random() * len(cls.baralho)) - 1
            cls.mao.append(cls.baralho[x])
            cls.baralho.pop(x)

    @classmethod
    def mostrar(cls, dealer=True):
        mao = cls.maoDoDealer if dealer else cls.mao
        if dealer:
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
        if not dealer:
            print("Carta do dealer:")
            print(
                f" _______ \n|{cls.maoDoDealer[0].naipe}      |\n|       |\n|   {cls.maoDoDealer[0].figura}  |\n|       |\n|______{cls.maoDoDealer[0].naipe}|\n")

    @classmethod
    def somar(cls):
        for i in range(len(cls.mao)):
            Cartas.resultMao = cls.mao[i].valor + Cartas.resultMao
        print(f"A soma de suas cartas são: {Cartas.resultMao}")
        print("Desce mais uma ou para?")

    @classmethod
    def descer(cls, resp):
        if resp == "Desce":
            Cartas.distribuir(1)
            Cartas.mostrar()
            Cartas.resultMao = Cartas.resultMao + Cartas.mao[-1].valor
            print(f"A soma de suas cartas são: {Cartas.resultMao}")
            print("Desce mais uma ou para?")
            return True
        else:
            print(f"Você parou com: {Cartas.resultMao}")
            return False
