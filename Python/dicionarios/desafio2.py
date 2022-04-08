# Criar um dicionário com os nomes e telefones de 10 pessoas.
# Solicitar um input para o USUÁRIO de uma letra.
# Verificar entre as chaves do dicionário se alguma delas começa com a letra inserida (se SIM retorna todas as chaves existentes que começam com essa letra).
# Solicitar um input para o USUÁRIO de 2 números.
# Verificar entre os valores do dicionário se algum deles começa com o primeiro número inserido e termina com o segundo números inserido (se SIM retorna todos os valores existentes que começam e terminam com esses inputs).

dicionario = {'Daniel':10983348844,'Miura':19078874632,
              'João':19078214632,'Douglas':19908274332,
              'guilherme':19978804632,'juninho':19910874632,
              'josias':19978874002,'jesimone':19978464602,
              'jabuti':19978674602,'lolinda':19978854632,
              'mãe':19978877630,'pai':19978874602,
              'tio':19908874672,'avô':19978874630 }

print("=-=-=-=-=-=-=- AGENDA TELEFONICA =-=-=-=-=-=-=-")
while True:
    nome = input("Digite uma letra: ")

    for key in dicionario.keys():

        if key[0] == nome.lower():
            print("\n%s: %s" % (key, dicionario[key]))
        else:
            pass