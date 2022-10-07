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
    resultDealer = 0

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
    def distribuir(cls, numero, dealer=False):
        mao = cls.maoDoDealer if dealer else cls.mao
        for i in range(numero):
            x = math.ceil(random.random() * len(cls.baralho)) - 1
            mao.append(cls.baralho[x])
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
                f" _______ \n|{cls.maoDoDealer[0].naipe}      |\n|       |\n|   {cls.maoDoDealer[0].figura}  |\n|       |\n|______{cls.maoDoDealer[0].naipe}|\n")

    @classmethod
    def somar(cls, dealer=False):
        mao = cls.maoDoDealer if dealer else cls.mao
        # TODO: calculo do As
        result = 0
        for i in range(len(mao)):
            result = mao[i].valor + result
        if result <= 11 and len(list(filter(lambda x: x.figura == "A ", mao))) == 1:
            result += 10
        if dealer:
            cls.resultDealer = result
        else:
            cls.resultMao = result
            print(f"A soma de suas cartas são: {result}")
        return result

    @classmethod
    def decidir(cls):
        resp = input("Desce mais uma ou Para? \n")
        match resp:
            case "Desce":
                cls.distribuir(1)
                cls.mostrar()
                cls.somar()
                return True
            case "Para":
                print(f"Você parou com: {cls.resultMao}")
                print("Aguardando o resultado do dealer...")
                return False
            case "Separa":
                pass
                # TODO: Implementar o split
            case _:
                print("Comando Incorreto")

    @classmethod
    def resetJogo(cls):
        cls.resultMao = 0
        cls.resultDealer = 0
        cls.mao = []
        cls.maoDoDealer = []
