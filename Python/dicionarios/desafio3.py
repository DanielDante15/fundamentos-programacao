# Criar um dicionário onde o 	USUÁRIO insira um jogador, número de sets e os pontos realizado pelo jogador em cada set de acordo com os sets que ele jogou.
# Printar todas essas informações na tela após encerrar o cadastro(ÍNDICE, NOME DO JOGADOR E NÚMERO DE SETS).
# Gerar um índice para cada um dos jogadores.
# O USUÁRIO escolherá entre os índices o do jogador que ele quer todos os detalhes em um novo input.
# Depois do input imprima todos os detalhes de acordo com o índice selecionado (dados para imprimir: NOME DO JOGADOR, NUMERO DE SETS E OS PONTOS POR CADA SEt).
cadastro = {}
sets = []
points = []
while True:
    points.clear()
    jogador = input("Digite o nome de um jogador:")
    sets = int(input("Digite o número de sets que o jogador participou: "))
    for i  in range(sets):
        pontos = int(input(f"Digite a quantidade de pontos feitos pelo {jogador} no {i+1}° set"))
        points.append(pontos)
    cadastro.update({jogador:points.copy()})
    print(cadastro)
    for i in cadastro:
        print(i)

