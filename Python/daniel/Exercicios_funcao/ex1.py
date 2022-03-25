def funcao():
    numero1 = 10
    numero2 = 20
    soma = numero1 + numero2
    print(soma)
    return soma


def funcao2(n1,n2):
    soma = n1 + n2
    print(soma)
def funcao3(n1=50,n2=20):
    soma = n1+n2
    print(soma)

def funcao4():
    n1 = 18
    n2 = 20
    soma = n1+n2
    return soma


def encontrarletra(palavra,letra):
    posicoes = []
    newword = list(palavra)
    print(newword)
    for i in range(0,len(newword)):
        if newword[i] == letra:
            posicoes.append(i)
    lenindex = len(posicoes)
    return lenindex, posicoes




