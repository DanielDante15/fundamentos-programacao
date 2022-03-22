
while True:
    numeros = []
    lenlist = int(input("Digite quantos números quer inserir: "))
    xnum = int(input("Digite o número a ser buscado: "))
    found = False
    pos = 0
    for i in range(lenlist):
        num = int(input(f'Digite o {i+1} número: '))
        numeros.append(num)
    while pos < len(numeros):
        if numeros[pos] == xnum:
            found = True
            print(f"Encontrou o número {xnum} na {pos+1} posição")
            break

        else:
            pos+=1

    if found == False:
        print("-1")


