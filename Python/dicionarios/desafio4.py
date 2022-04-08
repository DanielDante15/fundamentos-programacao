# Crie 3 DICIONÁRIOS: lanches, bebidas e sobremesas e uma LISTA pedido.
# Criar uma função de pedido para cada um (na função ele deve dar um cardápio para o usuário com índices de cada elemento).
# O usuário insere o ÍNDICE e em seguida o PEDIDO é printado na tela e ARMAZENADO na LISTA PEDIDO de acordo com o elemento.
# Continua ->


# Após realizados os três pedidos com as três funções, vai ser criada uma função para FINALIZAR o pedido.
# Nela você pede para o USUÁRIO verificar se o pedido está correto e se ele deseja mais alguma coisa (se SIM o código deve voltar as funções de pedido novamente).
# Se ele dizer que o pedido está correto você deve finalizar o pedido e SALVAR A LISTA  em um ARQUIVO .txt que será a comanda (comanda.txt)



lan = {
    '1':{
        'nome' : 'Big Mac',
        'valor': 18.90
    },
    '2':{
        'nome' : 'Mc Chicken',
        'valor': 14.90
    },
    '3':{
        'nome' : 'McNuggets',
        'valor': 19.90
    },
    '4':{
        'nome' : 'Mcnífico',
        'valor': 29.90
    },
    '5':{
        'nome' : 'Quarteirão',
        'valor': 14.90
    },
    '6':{
        'nome' : 'Big Tasty',
        'valor': 24.90
    },
}
beb = {
    '1':{
        'nome' : 'Coca Cola',
        'valor': 10.00
    },
    '2':{
        'nome' : 'Fanta Laranja',
        'valor': 8.90
    },
    '3':{
        'nome' : 'Sprite',
        'valor': 7.90
    },
    '4':{
        'nome' : 'Suco de Uva',
        'valor': 12.90
    },
    '5':{
        'nome' : 'Água',
        'valor': 4.90
    },
}
sob= {
    '1':{
        'nome' : 'Casquinha',
        'valor': 2.50
    },
    '2':{
        'nome' : 'McColosso',
        'valor': 4.00
    },
    '3':{
        'nome' : 'McFlury',
        'valor': 10.00
    },
    '4':{
        'nome' : 'McShake',
        'valor': 12.00
    },

}
# print(lan)
# print(lan['1'])
# print(list(lan['1'].keys())[0])
# print(lan['1']['nome'])
# print(lan['1']['valor'])




def cardapio(lan, beb, sob):
    while True:
        escolha = input("digite o que deseja:")
        if escolha.lower() == 'lanches':
            lanches(lan)
            entrada = int(input("Digite o número do lanche: "))


            print("\n")

        elif escolha.lower() == 'bebidas':
            bebidas(beb)
            print("\n")
        elif escolha.lower() == 'sobremesas':
            sobremesas(sob)
            print("\n")
        elif escolha.lower() == 'tudo':
            lanches(lan)
            bebidas(beb)
            sobremesas(sob)
        else:
            print("Iten não encontrado, tente novamente!")


def lanches(lan):
    print("----------------- LANCHES -----------------")
    for i in lan.keys():
        print(i, end="-")
        print(lan[i]['nome'], end=" -------- ")
        print(f"R${lan[i]['valor']}")

    print("-------------------------------------------\n")


def bebidas(beb):
    print("------------------ BEBIDAS ----------------")
    for i in beb.keys():
        print(i, end="-")
        print(beb[i]['nome'], end=" -------- ")
        print(f"R${beb[i]['valor']}")
    print("-------------------------------------------\n")


def sobremesas(sob):
    print("--------------- SOBREMESAS ----------------")
    for i in sob.keys():
        print(i, end="-")
        print(sob[i]['nome'], end=" -------- ")
        print(f"R${sob[i]['valor']}")
    print("-------------------------------------------\n")


cardapio(lan,beb,sob)




