from Cartas import Cartas


def Jogar(quantBar=True, reiniciar=False):
    if quantBar == True:
        x = int(input('Escolha quantos baralhos: '))
    else:
        x = Cartas.numeroDeBaralhos

    if x > 0 and x < 3:
        if reiniciar == False:
            print("Embaralhando...")
            print("Aqui estão suas cartas:")
            Cartas.addBaralho(x)

        if reiniciar == True:
            print("Rembaralhando...")
            print("novas cartas:")

        Cartas.distribuir(2)
        Cartas.mostrar()
        Cartas.somar()

        resp = input()
        retorno = Cartas.decidir(resp)
        while retorno:
            if Cartas.resultMao > 21:
                print("Sua soma estourou! O Dealer venceu!")
                Cartas.resultMao = 0
                Cartas.mao = []
                Jogar(quantBar=False, reiniciar=True)
            if Cartas.resultMao == 21:
                print("BLACK JACK!")
                Cartas.resultMao = 0
                Cartas.mao = []
                Jogar(quantBar=False, reiniciar=True)
            else:
                resp = input()
                retorno = Cartas.decidir(resp)

    else:
        print("Valor incorreto, tente um algarismo entre 1 e 2")
        Jogar(quantBar=True, reiniciar=False)
