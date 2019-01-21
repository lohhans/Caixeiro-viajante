from matriz import Matriz
from ponto import Ponto
from caixeiroViajante import *
from datetime import datetime

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

print("Problema bitônico euclidiano do caixeiro-viajante:")
matriz.mostrarMatriz(matriz) #Print da matriz
print(" ")

# Registra o momento antes da execução do algoritmo
t0 = datetime.now()

# Roda o algoritmo 10 vezes
for k in range(10):
    resp = caixeiroViajanteBT(matriz) #Realiza o caminho bitônico

# Registra o momento apos a execução do algoritmo
t1 = datetime.now()

# Calcula a o tempo de execucao em milissegundos da operacao
diff = t1 - t0
tempo = (diff.total_seconds() * 1000) / k

printArray(resp) #Print do caminho
print(" ")

# Exibe resultado do teste
print("Média de tempo do Algoritmo Backtracking executado 10 vezes: " + str(tempo) + " ms")
