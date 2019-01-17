from matriz import Matriz
from ponto import Ponto
from caixeiroViajante import *

matriz = Matriz(9)

ponto1 = Ponto('A')
ponto2 = Ponto('B')
ponto3 = Ponto('C')
ponto4 = Ponto('D')
ponto5 = Ponto('E')
ponto6 = Ponto('F')
ponto7 = Ponto('G')
ponto8 = Ponto('Y')
ponto9 = Ponto('X')
ponto10 = Ponto('Z')

matriz.inserirElemento(0,0,ponto1)
matriz.inserirElemento(6,1,ponto2)
matriz.inserirElemento(3,2,ponto3)
matriz.inserirElemento(2,5,ponto4)
matriz.inserirElemento(5,6,ponto5)
matriz.inserirElemento(1,7,ponto6)
matriz.inserirElemento(4,8,ponto7)
matriz.inserirElemento(0,1,ponto8)
matriz.inserirElemento(0,2,ponto9)
matriz.inserirElemento(0,3,ponto10)

matriz.mostrarMatriz(matriz)

print(" ")

resp = gerarCaminho(matriz)
printArray(resp)
