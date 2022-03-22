def main():

    while True:
        num = int(input("Digite um número: "))
        comparar = num
        x = [int(a) for a in str(num)]
        calculo = 0
        for i in range( len(x)):
            calculo += x[i]** len(x)

        if calculo == comparar:
            print("esse número é armstrong")
            continue
        else:
            print("esse número não é armstrong")
            continue

    print(comparar)
    print(calculo)

main()