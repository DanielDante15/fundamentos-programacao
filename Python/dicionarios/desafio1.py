dicionario = {}
bissexto = []
chave = int(input("Digite um índice: "))
for i in range(chave):
    valor = int(input("Digite um ano"))
    dicionario.update({f'indice{i+1}': valor})

    if (valor % 4==0 and valor % 100!=0) or (valor % 400==0):

        bissexto.append(valor)
    else:
        pass

print(dicionario)
print(f'os anos bissextos são {bissexto}')