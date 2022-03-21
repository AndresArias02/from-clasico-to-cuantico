import math
import matplotlib.pyplot as plt

def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def accionmatrizvector(A,v):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma = suma + A[i][j] * v[j][0]
        matriz = matriz + [suma]
    return matriz

def multcplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)



def productomatricesComplex(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = (0,0)
            for k in range(columnas):
                suma = sumacplx(suma, multcplx(A[i][k], B[k][j]))
            fila += [(suma)]
        matriz += [fila]
    return matriz

def modulocplx(a):
    return math.sqrt((a[0])**2 + (a[1])**2)


def productoMatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = 0
            for k in range(columnas):
                suma = suma + A[i][k] * B[k][j]
            fila += [suma]
        matriz += [fila]
    return matriz

def numero_de_estados(matriz):
    estados = []
    for i in range(len(matriz)):
        estados += [i]
    return estados

def accionmatrizvectorCplx(A,v):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = (0,0)
        for j in range(columnas):
            suma = sumacplx(suma, multcplx(A[i][j], v[j][0]))
        matriz = matriz + [(suma)]
    return matriz


def graficar_estados(estados, v):
    plt.bar(estados, v, facecolor = "deeppink")
    plt.title("Probabilidades del vector")
    plt.xlabel("Estados")
    plt.ylabel("Probabilidades")
    plt.show()
    plt.savefig('Graficasyscuantico.png')