import random

def main():
    print("Jogo de advinhação")
    life = 50
    num = randomize()

    v_f = False
    while v_f == False and life > 0:
        v_f, life = compare(num, life)
        print("Voce errou, tente novamente: ")




def guess(life):
    guess_number = int(input("Digite um numero: "))
    return guess_number, life



def randomize():
    rand_number = random.randint(0,101)
    print(rand_number)
    return rand_number


def compare(num,life):
    guess_number, life = guess(life)
    if num == guess_number :
        print("Voce ganhou, parabéns!!")
        return True, life
    else:
        life = life - (guess_number - num)
        return False, life
main()