from OperacionesElementales import *
from fractions import Fraction

def revisarPrimerUno(fila, indiceAnterior):
    cont = 0
    for i in fila:
        if i != 0:
            if i == 1 and cont > indiceAnterior:
                return {"b":1, "c":cont}
            return {"b":0,"c":cont}
        cont+=1
    return {"b":1, "c":-1}

def validarUnosArriba(index, matriz):
    copyIndex = [0, 0]
    copyIndex[0] = index[0]
    copyIndex[1] = index[1]
    index[0] -= 1
    while index[0] >= 0:
        valor = matriz[index[0]][index[1]]
        if valor != 0:
            matriz = sumaDeFilas(matriz, index[0], copyIndex[0], (valor*-1))
        index[0] -= 1
    index[0] = copyIndex[0]
    index[0] += 1
    while index[0] < len(matriz):
        valor = matriz[index[0]][index[1]]
        if valor != 0:
            matriz = sumaDeFilas(matriz, index[0], copyIndex[0], (valor * -1))
        index[0] += 1
    return matriz

def buscarFilaNula(fila):
    for i in fila:
        if i != 0:
            return False
    return True

def getUnos(matriz):
    unos = []
    contFila = 0
    for fila in matriz:
        contColumna = 0
        for columna in fila:
            if columna == 1:
                unos += [[contFila, contColumna]]
                break
            contColumna += 1
        contFila += 1
    return unos

def revisarUno(index, matriz):
    copyIndex = [0,0]
    copyIndex[0] = index[0]
    copyIndex[1] = index[1]
    index[0] -= 1
    while index[0] >= 0:
        if matriz[index[0]][index[1]] != 0:
            return False
        index[0] -= 1
    index[0] = copyIndex[0]
    index[0] += 1
    while index[0]<len(matriz):
        if matriz[index[0]][index[1]] != 0:
            return False
        index[0] += 1
    return True

def revisar(matriz):
    if matriz[0][0]!=1:
        return False
    else:
        i = len(matriz)-1
        boolean = True
        filaAnteriorNula = buscarFilaNula(matriz[i])
        i-=1
        while i != 0:
            boolean = buscarFilaNula(matriz[i])
            if boolean and filaAnteriorNula:
                pass
            elif boolean and not filaAnteriorNula:
                return False
            else:
                filaAnteriorNula = boolean
            i-=1
        unos = getUnos(matriz)
        for uno in unos:
            if not revisarUno(uno, matriz):
                return False
    return True

def gaussJordan(matriz):
    if matrizNula(matriz):
        return matriz
    while not revisar(matriz):
        """
        El siguiente while sirve para poner un 1 en la fila 0 columna 0
        """
        while matriz[0][0] != 1:
            filaPosible = -1
            for i in range(1,len(matriz)):
                if matriz[i][0] == 1:
                    filaPosible = i
                    break
            if filaPosible != -1:
                matriz = intercambiarFilas(matriz, 0, filaPosible)
                print("Intercambia fila 0 con fila "+str(filaPosible))
            else:
                for i in range(1,len(matriz)):
                    if matriz[i][0] != 0:
                        constante = Fraction(1-matriz[0][0], matriz[i][0])
                        matriz = sumaDeFilas(matriz, 0, i, constante)
                        print("Suma fila 0 + fila: "+str(i)+"*"+str(constante))
                        break
                    else:
                        pass
                if matriz[0][0] != 1:
                    for i in range(1, len(matriz)):
                        if matriz[i][0] != 0:
                            constante = 1/matriz[i][0]
                            matriz = multiplicarPorConstante(matriz, 0, constante)
                            print("Hace fila 0 * "+str(constante))
                            break
                        else:
                            pass
                else:
                    break
        """
        Ahora procedemos a poner 0 debajo de fila 0 columna 0
        Asumo que en fila 0 columna 0 queda un 1
        """
        for i in range(1, len(matriz)):
            constante = matriz[i][0]*-1
            if constante != 0:
                matriz = sumaDeFilas(matriz, i, 0, constante)
                print("Suma fila: " + str(i) + " fila: 0 * "+str(constante))
        """
        Ahora procedemos a revisar el resto de filas y columnas
        """
        unoAnterior = -1
        cont = 0
        for fila in matriz:
            aux = unoAnterior
            result = revisarPrimerUno(fila, unoAnterior)
            booleanRetorno = result.get("b")
            unoAnterior = result.get("c")
            #Primer valor de la fila es 1 procedemos a revisar que sea el unico elemento de su columna
            if unoAnterior == -1:
                unoAnterior == aux
            elif booleanRetorno:
                matriz = validarUnosArriba([cont, unoAnterior], matriz)
            #Primer valor de la fila es != de uno procedemos a hacerlo uno
            else:
                constante = Fraction(1, fila[unoAnterior])
                matriz = multiplicarPorConstante(matriz, cont, constante)
                matriz = validarUnosArriba([cont, unoAnterior], matriz)
            cont+=1
    return matriz

def matrizNula(matriz):
    matriz0 = True
    for fila in matriz:
        for columna in fila:
            if columna != 0:
                matriz0 = False
    return matriz0

#print(gaussJordan([[1, -1, -1, -2], [0, 1, 0, 1], [2, -3, 5, 1]]))
