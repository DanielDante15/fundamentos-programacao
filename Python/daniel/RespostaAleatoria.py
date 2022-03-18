import random
while True:
    question = input("Faça uma pergunta: ")
    randnumber = random.randint(0,10)

    if randnumber % 2 == 0:
        print("Não")
    else:
        print("Sim")