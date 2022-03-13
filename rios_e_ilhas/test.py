#!/usr/bin/python3

from algoritmo import encontrar_rios_e_ilhas

matrix1 = [ \
    [1, 0, 0, 1, 0],\
    [1, 0, 1, 0, 0],\
    [0, 0, 1, 0, 1],\
    [1, 0, 1, 0, 1],\
    [1, 0, 1, 1, 0],\
]

gabarito1 = [1, 2, 2, 2, 5] 

def comparar_se_valores_sao_iguais(valor1, valor2):
    if (valor1 == valor2):
        return True
    return False

def verificar_rios_com_gabarito(rios, gabarito):
    if (comparar_se_valores_sao_iguais(len(gabarito),len(rios)):
        for val in range(len(gabarito)):
            if (!comparar_se_valores_sao_iguais(gabarito[val],rios[val])):
                return False
        return True
    return False

def main():
    rios = []
    ilhas = []
    rios, ilhas = encontrar_rios_e_ilhas(matrix1)
    if (verificar_rios_com_gabarito(rios,gabarito1)):
        print("Resultado OK")
    else:
        print("Resultado errado")

if __name__ == "__main__":
    main()


