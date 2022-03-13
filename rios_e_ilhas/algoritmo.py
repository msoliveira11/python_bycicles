#!/usr/bin/python3

def encontrar_rios(matrix_mapa, linha, coluna, soma):

    # se encontrar terra
    if (matrix[linha][coluna] == 0):
        return 0

    # se sair do range da linha
    if (len(matrix[linha]) < coluna):
        return 0

    # se sair do range da coluna
    if (len(matrix) < linha):
        return 0

    # andar para direita
    soma += encontrar_rios(matrix_mapa,linha,coluna+1,soma)

    # andar para baixo
    soma += encontrar_rios(matrix_mapa,linha+1,coluna,soma)

    # andar para esquerda
    soma += encontrar_rios(matrix_mapa,linha,coluna-1,soma)

    # andar para cima
    soma += encontrar_rios(matrix_mapa,linha-1,coluna,soma)

    return 1

    return soma

def encontrar_rios_e_ilhas(matrix_mapa):
    rios = []
    ilhas = []
    return rios, ilhas
