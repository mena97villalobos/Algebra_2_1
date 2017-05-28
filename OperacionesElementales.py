def intercambiarFilas(matriz, fila1, fila2):
    tmp1 = matriz[fila1]
    matriz[fila1]=matriz[fila2]
    matriz[fila2]=tmp1
    return matriz

def multiplicarPorConstante(matriz, filaC, constante):
    fila = matriz[filaC]
    for i in range(0,len(fila)):
        fila[i] = fila[i]*constante
    matriz[filaC] = fila
    return matriz

def sumaDeFilas(matriz, filaS, filaC, constante):
    fila1 = matriz[filaS]
    fila2 = matriz[filaC]
    for i in range(0, len(matriz[0])):
        fila1[i] += fila2[i]*constante
    matriz[filaS]=fila1
    return matriz