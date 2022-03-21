import libreria3 as afaa
import math

def main():

    print("Experimento canicas con coeficientes boolenaos")
    Matriz = [[0,0,0,0,1,0],[0,0,0,1,0,0],
            [0,0,0,0,0,0],[1,0,0,0,0,0],
            [0,0,1,0,0,0],[0,1,0,0,0,1]]
    for i in Matriz:
        print(i)
    ticks = 4
    X = [x[:] for x in Matriz]
    for i in range(2,ticks+1):
        X = afaa.productoMatrices(X,Matriz)
    print("Estado inicial: ")
    Estado_inicial = [[6],[0],[5],[3],[1],[4]]
    for x in Estado_inicial:
        print(Estado_inicial)
    posicion = afaa.accionmatrizvector(X, Estado_inicial)
    print("Canicas presentes en cada caja: ")
    print(posicion)

    print("Sistemas cuanticos probabilisticos")
    Matriz = [[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],[(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
            [(1/math.sqrt(2),0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],[(0,0), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (1,0), (0,0), (0,0), (0,0), (0,0)],
            [(0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0), (0,0)],[(0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (-1/math.sqrt(6),1/math.sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0)],
            [(0,0), (0,0), (-1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (1,0), (0,0)],[(0,0), (0,0), (1/math.sqrt(6),-1/math.sqrt(6)), (0,0), (0,0), (0,0), (0,0), (1,0)]]
    for i in Matriz:
        print(i)
    ticks = 3
    X = [x[:] for x in Matriz]
    for i in range(2, ticks + 1):
        X = afaa.productomatricesComplex(X, Matriz)
    print("Estado inicial del sistema: ")
    Estado_inicial= [[(1,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]]
    for i in Estado_inicial:
        print(i)
    posicion = afaa.accionmatrizvectorCplx(X, Estado_inicial)
    print("Probabilidades de caer en la posicion: ")
    probabilidades_posicion = []
    for i in range(len(posicion)):
        probabilidades_posicion += [(afaa.modulocplx(posicion[i]))**2]
    for i in probabilidades_posicion:
        print(i)
    afaa.graficar_estados(afaa.numero_de_estados(Matriz), probabilidades_posicion)
main()