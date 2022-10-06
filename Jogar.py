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
        Cartas.distribuir(2, dealer=True)
        Cartas.mostrar()
        Cartas.somar()

        retorno = True
        while retorno:
            if Cartas.resultMao > 21:
                print("Sua soma estourou! O Dealer venceu!")
                Cartas.resetJogo()
                Jogar(quantBar=False, reiniciar=True)
            if Cartas.resultMao == 21:
                print("BLACK JACK!")
                Cartas.resetJogo()
                Jogar(quantBar=False, reiniciar=True)
            else:
                Cartas.somar(True)
                while Cartas.resultDealer < 17:
                    Cartas.distribuir(1, dealer=True)
                if Cartas.resultDealer > 21:
                    print("O Dealer estourou! Voce venceu!")
                elif Cartas.resultDealer == 21:
                    print("O Dealer conseguiu um BlackJack! O Dealer venceu!")
                else:
                    if Cartas.resultDealer == Cartas.resultMao:
                        print("O jogo empatou!")
                    elif Cartas.resultDealer > Cartas.result:
                        print("O Dealer venceu, com um total de:" +
                              Cartas.resultDealer)
                    else:
                        print("Voce venceu com um total de:" + Cartas.resultMao)
                Cartas.resetJogo()
                # TODO: Opcao de jogar denovo
                retorno = Cartas.decidir()

    else:
        print("Valor incorreto, tente um algarismo entre 1 e 2")
        Jogar(quantBar=True, reiniciar=False)
