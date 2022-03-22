def main():


    inicial = int(input("Digite o primeiro número: "))
    final = int(input("Digite o ultimo número: "))

    armstrong = []
    for  i in range(inicial,final+1):


        num = i
        comparar = num
        x = [int(a) for a in str(num)]
        calculo = 0
        for i in range( len(x)):
            calculo += x[i]** len(x)

        if calculo == comparar:
            armstrong.append(num)

    print(armstrong)



main()