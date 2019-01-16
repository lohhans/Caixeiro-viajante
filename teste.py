from matriz import Matriz
from ponto import Ponto
from caixeiroViajante import *

matriz = Matriz(5,5)

ponto1 = Ponto('A')
ponto2 = Ponto('B')
ponto3 = Ponto('C')
ponto4 = Ponto('D')
ponto5 = Ponto('E')
ponto6 = Ponto('F')
ponto7 = Ponto('G')


matriz.inserirElemento(0,1,ponto1)
print(matriz.elementos[0][1].nome)
matriz.inserirElemento(2,2,ponto2)
print(matriz.elementos[2][2].nome)
matriz.inserirElemento(2,3,ponto3)
print(matriz.elementos[2][3].nome)
matriz.inserirElemento(3,3,ponto4)
print(matriz.elementos[3][3].nome)
matriz.inserirElemento(3,4,ponto5)
print(matriz.elementos[3][4].nome)
matriz.inserirElemento(4,2,ponto6)
print(matriz.elementos[4][2].nome)
matriz.inserirElemento(3,0,ponto7)
print(matriz.elementos[3][0].nome)
print(" ")

matriz.mostrarMatriz(matriz,5,5)
#
# resultado = []
# resultado = caixeiroViajante(matriz, ponto2)
# mostrarResultado(resultado)
