

dicionario = {}
lista = ["Trabalho","Sucesso","Dicionário"]

for i in range(len(lista)):
    dicionario[f"chave{i+1}"] = lista[i]
print(dicionario)
print(f'o Único lugar onde o {dicionario["chave2"]} vem antes do {dicionario["chave1"]} é no {dicionario["chave3"]}')