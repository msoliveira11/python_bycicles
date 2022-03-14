#!/usr/bin/python3

from algoritmo import encontrar_rios_e_ilhas

matrix1 = [ \
    [1, 0, 0, 1, 0],\
    [1, 0, 1, 0, 0],\
    [0, 0, 1, 0, 1],\
    [1, 0, 1, 0, 1],\
    [1, 0, 1, 1, 0],\
]

matrix2 = [ \
        [1,0],\
        [0,1],\
        ]

matrix3 = [ \
        [1,1,0],\
        [0,1,0],\
        [0,1,1],\
        ]

mapas = []
mapas.append(matrix1)
mapas.append(matrix2)
mapas.append(matrix3)

gabarito_rios_1 = [1, 2, 2, 2, 5] 
gabarito_rios_2 = [1, 1] 
gabarito_rios_3 = [5]

gabarito_rio = []
gabarito_rio.append(gabarito_rios_1)
gabarito_rio.append(gabarito_rios_2)
gabarito_rio.append(gabarito_rios_3)

gabarito_ilha_1 = [7, 5, 1]
gabarito_ilha_2 = [1, 1]
gabarito_ilha_3 = [2, 2]

gabarito_ilha = []
gabarito_ilha.append(gabarito_ilha_1)
gabarito_ilha.append(gabarito_ilha_2)
gabarito_ilha.append(gabarito_ilha_3)

def ordenar_lista(entrada):
    entrada.sort()
    return entrada

def comparar_se_valores_sao_iguais(valor1, valor2):
    if (valor1 == valor2):
        return True
    return False

def verificar_com_gabarito(lista, gabarito):
    lista = ordenar_lista(lista)
    gabarito = ordenar_lista(gabarito)
    if (comparar_se_valores_sao_iguais(len(gabarito),len(lista))):
        for val in range(len(gabarito)):
            if ((comparar_se_valores_sao_iguais(gabarito[val],lista[val]))==False):
                return False
        return True
    return False

def realizar_testes(mapas, gabarito_rio, gabarito_ilha):
    for teste in range(len(mapas)):
        rios = []
        ilhas = []
        rios, ilhas = encontrar_rios_e_ilhas(mapas[teste])
        print("Teste " + str(teste) + ":")
        #print(rios)
        #print(gabarito_rio[teste])
        if (verificar_com_gabarito(rios,gabarito_rio[teste])):
            print("Resultado de rios OK")
        else:
            print("Resultado de rios errado")
        #print(ilhas)
        #print(gabarito_ilha[teste])
        if (verificar_com_gabarito(ilhas,gabarito_ilha[teste])):
            print("Resultado de ilhas OK")
        else:
            print("Resultado de ilhas errado")

def main():
    realizar_testes(mapas, gabarito_rio, gabarito_ilha)

if __name__ == "__main__":
    main()


