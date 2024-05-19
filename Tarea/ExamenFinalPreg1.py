"""Escriba una función que reciba dos matrices y devuelva la resta, sin utilizar ninguna librería especial de Python como
numpy o similares."""

# entrada: Necesito las Matrices A y B

#Proceso = restar a[0]- b[0] a[1]-b[1] 


def Matrices():
    MatrizA = [[1, 2, 3], [14, 15, 16]]
    MatrizB = [[2, -7, -4], [7, -1, -8]]
    return MatrizA, MatrizB

def main(): 
    MatrizA, MatrizB = Matrices()
    resultado = []

    for i in range(len(MatrizA)):
        fila_resultado = []
        for j in range(len(MatrizA[0])):
            resta = MatrizA[i][j] - MatrizB[i][j]
            fila_resultado.append(resta)
        resultado.append(fila_resultado)

    for fila in resultado: 
        print(fila)


if __name__ == "__main__": 
    main()


