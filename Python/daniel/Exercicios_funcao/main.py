import ex1

if __name__ == '__main__':
    while True:
        # ex1.funcao()
        # numero1 = 15
        # numero2 = 20
        # ex1.funcao2(n1=numero1,n2=numero2)
        # ex1.funcao3()
        # retorno = ex1.funcao4()
        # print(retorno)
        word = input("Digite uma palavra:")
        letter = input("Digite a letra que quer buscar: ")
        if word.upper() == "EXIT" or letter.upper() == "EXIT":
            break
        else:
            len, ind = ex1.encontrarletra(word, letter)
            print(len)
            print(ind)

