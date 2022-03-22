import random

def main():
    print('JOGO DA ADVINHAÇÃO')
    life = 50
    attempts = 3
    win = False
    randnum = random.randint(0,101)
    while (attempts > 0 and life > 0):
        print(randnum)
        guess_number = guess()
        if guess_number == randnum:
            print("Parabéns, você ganhou!!!")
            win = True
            break
        else:
            print("Resposta errada")
            attempts -= 1
            life -= abs(randnum - guess_number)
            print(f'A sua vida é de {life}')
            print(f'Você tem {attempts} tentativas')
    if win == False:
        print('Voce perdeu!!!')

def guess( ):
    num = int(input("Digite um Número:"))

    return num

main()