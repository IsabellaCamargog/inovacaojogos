import random

def jogar():
    print("******************")
    print("Bem vindo a Forca!")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_objetivo = palavras[numero].upper()

    letras_encontradas = ["_" for letra in palavra_objetivo]

    enforcado = False
    acerto = False
    erros = 0

    print(letras_encontradas)

    while(not enforcado and not acerto):
        chute = input("Qual seu chute de letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_objetivo):
            index = 0
            for letra in palavra_objetivo:
                if(chute == letra):
                    letras_encontradas[index] = letra
                index += 1
        else:
            erros += 1
            forca(erros)

        enforcado = erros == 7
        acerto = "_" not in letras_encontradas

        #print(palavra_objetivo)
        print(letras_encontradas)

    if(acerto):
        print("Parabéns, voceê é foda")
        imprime_venceu()
    else:
        print("Voce eh a verrrrgonha da prrrofison")
        imprime_perdeu(palavra_objetivo)
    print("END GAME")

def imprime_perdeu(palavra_objetivo):
    print(f"A palavra era {palavra_objetivo}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def imprime_venceu():
    print("Parabéns, você venceu!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()