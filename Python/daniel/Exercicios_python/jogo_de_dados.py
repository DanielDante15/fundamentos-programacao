import random

def main():
    saldo = 20.0
    pontosplayer = 0
    revanche = 0
    pontospc = 0

    while True:

        if revanche == 1:
            if pontosplayer == 4:
                saldo+=20
                ask = input("Deseja jogar novamente?(S/N)")
                if ask.upper() == 'S':
                    pontosplayer = 0
                    pontospc = 0

        rand_number = random.randint(1, 6)

        print("-----------Jogo de Dados-----------")
        print (f'seu saldo é de: {saldo}')
        print(rand_number)

        while True:
            pnum1 = int(input("Digite um número de 1 a 6:"))
            if pnum1 > 6 or pnum1 < 1:
                print("O número que você digitou não é válido")
                continue
            pnum2 = int(input("Digite  mais um número de 1 a 6:"))
            if pnum2 > 6 or pnum2 < 1:
                print("O número que você digitou não é válido")
                continue
            print("*"*100)
            break

        print("*" * 100)
        pcnum1,pcnum2 = cpunumber(pnum1,pnum2)

        if pnum1 == rand_number or pnum2 == rand_number:
            pontosplayer += 1
            print(f'voce tem {pontosplayer} pontos')

        elif pcnum1 == rand_number or pcnum2 == rand_number:
            pontospc += 1
            print(f'o pc tem {pontospc} pontos')
        else:
            print("Ninguem acertou")

        if pontospc == 2:
            print("O pc ganhou!!")
            saldo -= 7.5
            continue
        if pontosplayer == 2:
            print("Voce ganhou!!")
            o = input("O pc quer revache, voce aceita? (S/N)")
            if o.upper() == 'S':
                revanche +=1
            else:
                saldo += 15
                pontosplayer = 0
                continue

def cpunumber(pnum1,pnum2):
    while True:
        cpunumber1 = random.randint(1,6)
        if cpunumber1 == pnum1 or cpunumber1 == pnum2:
            continue
        break
    while True:
        cpunumber2 = random.randint(1,6)
        if (cpunumber2 == cpunumber1) or (cpunumber2 == pnum1) or (cpunumber2 == pnum2):
            continue
        break
    print(f'NUMERO DA CPU 1 = {cpunumber1}')
    print(f'NUMERO DA CPU 2 = {cpunumber2}')
    return cpunumber1,cpunumber2

main()