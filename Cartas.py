import math
import random


class Cartas:
    def __init__(self, naipe, figura, valor):
        self.naipe = naipe
        self.figura = figura
        self.valor = valor

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
    def mostrar(cls):
        for i in range(len(cls.mao)):
            print(" _______ ")
            print(f"|{cls.mao[i].naipe}      |")
            print("|       |")
            print(f"|   {cls.mao[i].figura}  |")
            print("|       |")
            print(f"|______{cls.mao[i].naipe}|")

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
