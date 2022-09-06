from pdb import Restart
from Cartas import Cartas


def Jogar(x):
    if x > 0 and x < 3:
        print("Embaralhando...")
        print("Aqui estão suas cartas:")

        Cartas.addBaralho(x)
        Cartas.distribuir(2)
        Cartas.mostrar()
        Cartas.somar()

        resp = input()
        retorno = Cartas.descer(resp)

        while retorno:
            Cartas.descer()
            Cartas.somar()
            resp = input()
            retorno = Cartas.descer(resp)

    else:
        print("Valor incorreto, tente um algarismo entre 1 e 2")
        Restart
