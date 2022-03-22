def main():
    while True:
        call = input("Chame a função [DEC/BIN]:")

        if call.lower() == "bin":
            bin()
        elif call.lower() == "dec":
            dec()
        else:
            print("A função que você digitou não existe,digite novamente:")

def dec():
    while True:
        num = input("Digite um número em binário: ")

        if num.upper() == "SAIR":
            return
        else:
            x = [int(a) for a in str(num)]
            numeros = list(reversed(x))
            binario2 = 0
            for i in range(len(numeros)):
                binario = (2 ** i) * numeros[i]
                binario2 = binario2 + binario
            print(binario2)
        continue

def bin():
    while True:
        binario = []

        num =input("Digite um número em decimal : ")
        if num.upper() == "SAIR":
            return
        else:
            numi = int(num)
            while (numi >0):
                resto = numi % 2
                inteiro = numi // 2
                numi = inteiro
                binario.append(resto)
            reversedbin = list(reversed(binario))
            print(reversedbin)
        continue

main()

