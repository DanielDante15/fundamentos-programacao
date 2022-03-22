while True:
    nome = input("Digite uma palavra:")
    array = list(nome)
    newarray = list(reversed(array))

    if array == newarray:
        print("palindromo")

    else:
         print("nao palindromo")
