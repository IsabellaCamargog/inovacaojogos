import random

def jogar():

    print("*****************")
    print("bem-vindo ao jogo")

    #numero_objetivo = 99
    numero_objetivo = round(random.randrange(1,101))
    #print(f"o sorteado foi: {numero_objetivo}")
    numero_tentativas = 0
    tentativa = 1
    numero_pontos = 1000

    print("Dificuldade: ")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    dificuldade = int(input("Selecione o nível de difículdade: "))

    if(dificuldade == 1):
        numero_tentativas = 15
    elif(dificuldade == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    while(tentativa <= numero_tentativas):
        print(f"Mermao, voce está na tentativa: {tentativa}, de um total de: {numero_tentativas}.")
        chute_string = input("Qual seu chute? (1-100)")
        chute = int(chute_string)

        if(chute < 1 or chute > 100):
            print("cara, você digitou um número inválido... porra!")
            exit()

        acertou = chute == numero_objetivo
        maior = chute > numero_objetivo
        menor = chute < numero_objetivo

        print(f"Cara, voce chutou: {chute}")

        if(acertou):
            print(f"Você acertou! Parabéns! Você fez {numero_pontos}")
            break
        else:
            if(maior):
                print("Você errou, este numero é MAIOR!")
            elif(menor):
                print("você errou, este numero é MENOR")
            pontos_perdidos = 10
            numero_pontos -= pontos_perdidos

        tentativa += 1

    print(f"fim de jogo, o número era {numero_objetivo}")

if(__name__ == '__main__'):
    jogar()
