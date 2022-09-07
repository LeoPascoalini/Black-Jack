import math
import random


class Cartas:
    def __init__(self, naipe, figura, valor):
        self.naipe = naipe
        self.figura = figura
        self.valor = valor

    numeroDeBaralhos = 1
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
            case _:
                print("Comando Incorreto")
