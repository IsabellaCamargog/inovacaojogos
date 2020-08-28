import adivinhacao
import forca

def selecionar_jogo():
    print("Selecione o jogo que você quer jogar, 1 para Adivinhacao, e 2 para Forca")

    jogo_selecionado = int(input("Defina sua opção: "))

    if(jogo_selecionado == 1):
        adivinhacao.jogar()
    elif(jogo_selecionado == 2):
        forca.jogar()

if(__name__ == '__main__'):
    selecionar_jogo()
