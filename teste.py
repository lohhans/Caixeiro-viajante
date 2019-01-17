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


matriz.inserirElemento(0,0,ponto1)
matriz.inserirElemento(6,1,ponto2)
matriz.inserirElemento(3,2,ponto3)
matriz.inserirElemento(2,5,ponto4)
matriz.inserirElemento(5,6,ponto5)
matriz.inserirElemento(1,7,ponto6)
matriz.inserirElemento(4,8,ponto7)

matriz.mostrarMatriz(matriz)

print(" ")

pontos = resgatarPontos(matriz)
printArray(pontos)

pontos = ordenarPontosPorColuna(pontos)
printArray(pontos)

resp = gerarCaminho(matriz)
printArray(resp)
