import IO_custom as cin
import Matriz_custom as draw

''' Exemplo de Velha
1 1
2 2
3 3
2 1
2 3
3 2
1 2
1 3
3 1
'''

''' 
1 1
1 3
2 2
2 1
3 3
'''
def checa_vitoria( matriz, marcador ):
    '''
        Confere se a matriz quadrada
        que usamos como tabuleiro
        possui algum vencedor
    '''

    if not draw.matriz_quadrada(matriz):
        return None

    horizontal = False

    # linha  [konstante][]
    for linha in matriz:
        uniforme = True
        for coluna in linha:
            if coluna != marcador:
                uniforme = False
        if uniforme:
            horizontal = True

    if horizontal:
        return True

    # coluna [][konstante]
    vertical = False
    for index in range(len(matriz[0])):
        uniforme = True
        for linha in matriz:
            if linha[index] != marcador:
                uniforme = False
        if uniforme:
            vertical = True

    if vertical:
        return True

    # diagonal principal [i][i] 
    first_diagonal = True
    # diagonal secundária [i][j] sendo i + j == len(matriz[0]) - 1
    second_diagonal = True
    jindex = len(matriz[0]) - 1
    for index in range(len(matriz[0])):
        if matriz[index][index] != marcador:
            first_diagonal = False
        if matriz[index][jindex] != marcador:
            second_diagonal = False
        jindex -= 1

    if first_diagonal or second_diagonal:
        return True

    return False

tamanho = 3
tabuleiro = draw.gerar_matriz(tamanho,tamanho,' ')
# TODO: aumentar modularização da criação do tabuleiro

jogada = []
marcador = 'X'
# 1º X 2º O

game = True
index = -1

if not draw.matriz_quadrada(tabuleiro):
    print("ERROR")
else:
    index = tamanho**2

while game and index > 0:
    jogada_invalida = True
    
    print("\n   Joga", marcador)

    while jogada_invalida:
        jogada = cin.filtra_input(1,True)
        log = ""
        
        if len(jogada) < 2 :
            log = cin.update_log(log, "Input incompleto")
        elif not ('0' <= jogada[0] <= '9' and '0' <= jogada[1] <= '9'):
            log = cin.update_log(log, "Input inválido: CODE NOT A NUMBER")
        else:
            jogada = [int(jogada[0]), int(jogada[1])]

            if not 0 < jogada[0] <= len(tabuleiro):
                log = cin.update_log(log, "Index out of range: 1ª coordenada fora do tabuleiro")
            if not 0 < jogada[1] <= len(tabuleiro[0]):
                log = cin.update_log(log, "Index out of range: 2ª coordenada fora do tabuleiro")

            if log == "":
                if tabuleiro[jogada[0]-1][jogada[1]-1] != ' ':
                    log = cin.update_log(log, "Already in use: Coordenada em uso")

        if log == "":
            jogada_invalida = False
        else:
            print(log)
    
    tabuleiro[jogada[0]-1][jogada[1]-1] = marcador
    
    draw.imprime_matriz(tabuleiro)

    if( checa_vitoria(tabuleiro,marcador) ):
        game = False
    else:
        if( marcador == 'X' ):
            marcador = 'O'
        else:
            marcador = 'X'
    index -= 1

print("\n\n")

if not game and checa_vitoria(tabuleiro,marcador):
    print(" ", marcador, "venceu")
elif index == 0:
    print(" Deu Velha")
