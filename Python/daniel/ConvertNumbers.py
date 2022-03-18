


def main():
    while True:
        call = input("Chame a função:")

        if call.lower() == "bin":
            bin()
        elif call.lower() == "dec":
            dec()
        else:
            print("o comando que voce digitou esta inválido")


def dec():

    while True:
        num = int(input("Digite um número em binário: "))
        x = [int(a) for a in str(num)]
        numeros = list(reversed(x))
        binario2 = 0
        for i in range(len(numeros)):
            binario = (2 ** i) * numeros[i]
            binario2 = binario2 + binario
        print(binario2)
        return



def bin():
    while True:
        binario = []

        num = int(input("Digite um número em decimal : "))

        while (num >0):
            resto = num % 2
            inteiro = num // 2
            num = inteiro
            binario.append(resto)
        reversedbin = list(reversed(binario))
        print(reversedbin)
        return

main()