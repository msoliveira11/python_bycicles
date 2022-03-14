#!/usr/bin/python3

import copy

def prRed(skk): print("\033[91m{}\033[00m" .format(skk), end="")

# Mostrar passos?
mostrar_passos = False

# Definicoes de constantes
CONST_RIO = 1
CONST_ILHA = 0

def imprimir_matriz(matriz, linha_elem, coluna_elem):
    for lin in range(len(matriz)):
        print("[", end="")
        for col in range(len(matriz[0])):
            if ((lin == linha_elem) and (col == coluna_elem)):
                prRed(matriz[lin][col])
            else:
                print(str(matriz[lin][col]), end="")
            if (col != (len(matriz[0])-1)):
                print(",", end="")
        print("]")
    print()

def rodar_algoritmo_busca(matrix_mapa, linha, coluna, evitado):
   
    # se sair do range da coluna
    if ((len(matrix_mapa) <= linha) or (linha < 0)):
        return 0

    # se sair do range da linha
    if ((len(matrix_mapa[linha]) <= coluna) or (coluna < 0)):
        return 0

    # se encontrar terra
    if (matrix_mapa[linha][coluna] == evitado):
        return 0

    matrix_mapa[linha][coluna] = evitado

    if (mostrar_passos == True):
        imprimir_matriz(matrix_mapa,linha,coluna)

    return (1 + \
            # andar para direita
            rodar_algoritmo_busca(matrix_mapa,linha,coluna+1,evitado) + \
            # andar para baixo
            rodar_algoritmo_busca(matrix_mapa,linha+1,coluna,evitado) + \
            # andar para esquerda
            rodar_algoritmo_busca(matrix_mapa,linha,coluna-1,evitado) + \
            # andar para cima
            rodar_algoritmo_busca(matrix_mapa,linha-1,coluna,evitado))

def encontrar_rios_e_ilhas(matrix_mapa):
    rios = []
    ilhas = []
    soma_inicial = 0
    matrix_original = copy.deepcopy(matrix_mapa)
    for linha in range(len(matrix_mapa)):
        for coluna in range(len(matrix_mapa[linha])):
            tamanho_rio = rodar_algoritmo_busca(matrix_mapa, linha, coluna, CONST_ILHA)
            if (tamanho_rio > 0):
                rios.append(tamanho_rio)
            else:
                tamanho_ilha = rodar_algoritmo_busca(matrix_original, linha, coluna, CONST_RIO)
                if (tamanho_ilha > 0):
                    ilhas.append(tamanho_ilha)
    return rios, ilhas
